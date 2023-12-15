import os
from settings import logger

from pymongo import collection, MongoClient


def _connect_db() -> collection:
    """Получение клиента базы данных"""
    client = MongoClient(f"mongodb://mongo_1:{os.getenv('MONGO_DB_PORT')}")
    db = client["users_db"]
    my_collection = db["users_sales"]
    logger.info(f'_connect_db {my_collection=}')
    return my_collection
