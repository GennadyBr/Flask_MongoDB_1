from mongo_db_conn import _connect_db
from settings import logger


def fill_data() -> None:
    """Первоначальное заполнение базы данных примерами"""
    collection = _connect_db()
    count = collection.count_documents({})
    if not count:
        collection.insert_many([
            {"ID": 1, "Name": "Misha", "Year": 1990, "Salary": 2000},
            {"ID": 2, "Name": "Tolya", "Year": 1991, "Salary": 2200},
            {"ID": 3, "Name": "Alex", "Year": 1992, "Salary": 1800},
            {"ID": 4, "Name": "Mark", "Year": 1993, "Salary": 2500},
            {"ID": 5, "Name": "Sasha", "Year": 1994, "Salary": 3000}
        ])
        logger.info(f'Первоначальное заполнение. Добавлено {collection.count_documents({})} документов')
    else:
        logger.info(f'База уже содержит {count} документов')


if __name__ == '__main__':
    fill_data()
