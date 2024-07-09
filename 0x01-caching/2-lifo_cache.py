#!/usr/bin/env python3
"""
LIFO caching algorithm
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This is Last In First Out
    """
    def __init__(self):
        """
        This initializes the class
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds item to the order lists
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = self.order.pop(-1)
            del self.cache_data[last_item]
            print(f"DISCARD: {last_item}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the dictionary
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
