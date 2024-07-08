#!/usr/bin/env python3
"""
Basic Cache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This is the Basic Caching mechanism
    """
    def put(self, key, item):
        """
        Add item to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
