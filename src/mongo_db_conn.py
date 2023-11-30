import logging
import os

from pymongo import collection, MongoClient


def _connect_db() -> collection:
    """Получение клиента базы данных"""
    logging.info(f"{os.getenv('MONGO_DB_PORT')=}")
    client = MongoClient(f"mongodb://mongo:{os.getenv('MONGO_DB_PORT')}")
    db = client["users_db"]
    collection = db["users_sales"]
    return collection
