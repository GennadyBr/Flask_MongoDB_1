import os
from logger import logger

from pymongo import collection, MongoClient


def _connect_db() -> collection:
    """Получение клиента базы данных"""
    client = MongoClient(f"mongodb://mongo:{os.getenv('MONGO_DB_PORT')}")
    db = client["users_db"]
    collection = db["users_sales"]
    logger.info(f'_connect_db {collection=}')
    return collection
