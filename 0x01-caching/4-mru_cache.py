#!/usr/bin/env python3
"""
MRU caching algorithm
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Most Recently Used mechanism
    """
    def __init__(self):
        """
        This is an initialization class
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds item to the front of the queue
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recent = self.order.pop(0)
            del self.cache_data[most_recent]
            print(f"DISCARD: {most_recent}")

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
