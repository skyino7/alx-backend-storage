#!/usr/bin/env python3
"""
Function that lists all documents in a collection
"""

def list_all(mongo_collection):
    """
    List all documents in a collection
    """

    if mongo_collection is None:
        return None

    return list(mongo_collection.find())
