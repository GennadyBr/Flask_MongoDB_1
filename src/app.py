import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect

from mongo_db_conn import _connect_db
from settings import logger

load_dotenv()

app = Flask(__name__)


@app.route("/")
def show_user():
    """Вывод содержания базы данных на первой странице"""
    users = []
    collection = _connect_db()
    for user in collection.find():
        users.append({"id": user["ID"], "name": user["Name"], "year": user["Year"], "salary": user["Salary"]})
    logger.info(f'show_user {users=}')
    return render_template("users_list.html", users=users)


@app.route("/add", methods=['GET', 'POST'])
def add_user():
    """Добавление новой записи в базу данных"""
    if request.method == 'GET':
        return render_template("user_details.html", user={})
    if request.method == "POST":
        id = int(request.form["id"])
        name = request.form["name"]
        year = int(request.form["year"])
        salary = float(request.form["salary"])
        collection = _connect_db()
        new_user = {"ID": id, "Name": name, "Year": year, "Salary": salary}
        collection.insert_one(new_user)
        logger.info(f'POST {new_user=}')
        return redirect('/')


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update_user(id):
    """Обновление существующей записи в базе данных"""
    user_list = []
    collection = _connect_db()
    if request.method == 'GET':
        for user in collection.find({'ID': id}):
            user_list.append({"id": user["ID"], "name": user["Name"], "year": user["Year"], "salary": user["Salary"]})
            logger.info(f'GET {user_list=}')
            return render_template("user_details.html", user=user_list[0])
    if request.method == 'POST':
        name = request.form["name"]
        year = int(request.form["year"])
        salary = float(request.form["salary"])
        collection = _connect_db()
        condition = {'ID': id}
        update_value = {"$set": {"Name": name, "Year": year, "Salary": salary}}
        collection.update_one(condition, update_value)
        logger.info(f'POST {id=}, {update_value=}')
        return redirect("/")


@app.route("/delete/<int:id>")
def delete_user(id):
    """Удаление существующей записи в базе данных"""
    collection = _connect_db()
    collection.delete_one({"ID": id})
    logger.info(f'DELETE {id=}')
    return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('FLASK_PORT'), debug=True, template_folder='templates')
