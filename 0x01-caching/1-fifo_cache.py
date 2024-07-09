#!/usr/bin/env python3
"""
FIFO caching algorithm
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First In First Out mechanism
    """
    def __init__(self):
        """
        This is an initialization class
        """
        super.__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds item to the front of the queue
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
