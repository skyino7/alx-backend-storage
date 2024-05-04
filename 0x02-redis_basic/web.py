#!/usr/bin/env python3
"""
In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:). The core of
the function is very simple. It uses the requests module
to obtain the HTML content of a particular URL and returns
it. Start in a new file named web.py and do not reuse the
code written in exercise.py. Inside get_page track how many
times a particular URL was accessed in the key "count:{url}"
and cache the result with an expiration time of 10 seconds.
Tip: Use http://slowwly.robertomurray.co.uk to simulate a
slow response and test your caching.
"""

from functools import wraps
import requests
import redis

red = redis.Redis()


def url_access_count(method):
    """
    Counts the number of times a particular URL is accessed.
    """
    @wraps(method)
    def wrapper(url):
        """
        Wrapper function.
        """
        key = f"count:{url}"
        red.incr(key)
        red.expire(key, 10)

        cached = f"cached:{url}"
        value_cached = red.get(cached)
        if value_cached:
            return value_cached.decode("utf-8")

        html_content = method(url)
        red.setex(cached, 10, html_content)
        return html_content

    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """
    Get page content.
    """
    return requests.get(url).text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
