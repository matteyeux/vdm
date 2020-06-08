"""Config module for vmd."""

import pymongo


def setup_mongo() -> pymongo.mongo_client.MongoClient:
    """Setup mongo client."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client
