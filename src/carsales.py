from flask import Flask, render_template, request, redirect
from pymongo import MongoClient, collection

carsales = Flask(__name__)


def connect_db() -> collection:
    """Получение клиента базы данных"""
    client = MongoClient("mongodb://mongo:27017")
    db = client["cars_db"]
    collection = db["cars_sales"]
    return collection


def start_mongo_db() -> None:
    """Первоначальное заполнение базы данных примерами"""
    collection = connect_db()
    collection.insert_many([
        {"ID": 1, "Name": "Toyota Camry", "Year": 2018, "Price": 2000},
        {"ID": 2, "Name": "Honda Civic", "Year": 2019, "Price": 2200},
        {"ID": 3, "Name": "Chevrolet Silverado", "Year": 2017, "Price": 1800},
        {"ID": 4, "Name": "Ford F-150", "Year": 2020, "Price": 2500},
        {"ID": 5, "Name": "Nissan Altima", "Year": 2021, "Price": 3000}
    ])


@carsales.route("/")
def main():
    """Вывод содержания базы данных на первой странице"""
    cars = []
    collection = connect_db()
    for car in collection.find():
        cars.append({"id": car["ID"], "name": car["Name"], "year": car["Year"], "price": car["Price"]})
    return render_template("cars_list.html", cars=cars)


@carsales.route("/add", methods=['GET', 'POST'])
def add_car():
    """Добавление новой записи в базу данных"""
    if request.method == 'GET':
        return render_template("car_details.html", car={})
    if request.method == "POST":
        id = int(request.form["id"])
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        collection = connect_db()
        new_car = {"ID": id, "Name": name, "Year": year, "Price": price}
        collection.insert_one(new_car)
        return redirect('/')


@carsales.route("/update/<int:id>", methods=['GET', 'POST'])
def update_car(id):
    """Обновление существующей записи в базе данных"""
    cr = []
    collection = connect_db()
    if request.method == 'GET':
        for car in collection.find({'ID': id}):
            cr.append({"id": car["ID"], "name": car["Name"], "year": car["Year"], "price": car["Price"]})
            return render_template("car_details.html", car=cr[0])
    if request.method == 'POST':
        name = request.form["name"]
        year = int(request.form["year"])
        price = float(request.form["price"])
        collection = connect_db()
        condition = {'ID': id}
        updateval = {"$set": {"Name": name, "Year": year, "Price": price}}
        collection.update_one(condition, updateval)
        return redirect("/")


@carsales.route("/delete/<int:id>")
def delete_car(id):
    """Удаление существующей записи в базе данных"""
    collection = connect_db()
    collection.delete_one({"ID": id})
    return redirect('/')


if __name__ == '__main__':
    start_mongo_db()

    carsales.run(host="0.0.0.0", port=8080, debug=True)
