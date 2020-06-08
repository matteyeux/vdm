"""Config module for vmd."""

import pymongo


def setup_mongo() -> pymongo.collection.Collection:
    """Setup mongo client."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    vdm_database = client["vdm"]
    collection = vdm_database["booking"]
    return collection
