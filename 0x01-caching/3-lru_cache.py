#!/usr/bin/env python3
"""
LRU caching algorithm
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This is Least Recently Used (LRU) cache
    """
    def __init__(self):
        """
        This initializes the class
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds item to the order list
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the existing key to update its position later
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least recently used item
            least_recent = self.order.pop(0)
            del self.cache_data[least_recent]
            print(f"DISCARD: {least_recent}")

        # Add the new key and item to the cache
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Gets an item from the dictionary and updates the order list
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the order list
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
