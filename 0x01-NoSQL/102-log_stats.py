#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most
present IPs in the collection nginx of the database logs
"""

from pymongo import MongoClient


def log_stats():
    """
    top 10 of the most present IPs in
    the collection nginx of the database logs
    """
    client = MongoClient('localhost', 27017)
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    count_status = collection.count_documents({"method": "GET",
                                               "path": "/status"})
    print(f"{count_status} status check")

    # IPs
    print("IPs:")
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for i, ip in enumerate(top_ips):
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
