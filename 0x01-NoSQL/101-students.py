#!/usr/bin/env python3
"""
Function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    return mongo_collection.find().sort("averageScore", -1)
