#!/usr/bin/env python
"""
script that provides some stats about
Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def log_stats(logs):
    """
    Nginx logs stored in MongoDB
    """
    client: MongoClient = MongoClient('localhost', 27017)
    db = client.logs
    collection = db.nginx

    total_logs: int = collection.count_documents({})

    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"Methods:")
    for method in methods:
        count: int = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    count_status: int = collection.count_documents({"method": "GET",
                                                    "path": "/status"})
    print(f"{count_status} status check")


if __name__ == "__main__":
    log_stats(logs=None)
