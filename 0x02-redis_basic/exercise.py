#!/usr/bin/env python3
""" Cache module """

import uuid
import redis
from typing import Union, Callable, Optional


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Get data from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> Union[str, bytes]:
        """ Get data as string """
        return self.get(data, lambda x: x.decode('utf-8'))


    def get_int(self, data: bytes) -> Union[int, bytes]:
        """ Get data as integer """
        return self.get(data, lambda x: int(x))

