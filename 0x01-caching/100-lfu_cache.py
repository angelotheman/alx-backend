#!/usr/bin/env python3
"""
LFU caching algorithm
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used mechanism
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """
        Adds item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.frequency[key] += 1
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                min_freq = min(self.frequency.values())
                lfu_keys = [
                        k for k, v in self.frequency.items() if v == min_freq]
                # If multiple keys have the same frequency, use LRU among them
                if len(lfu_keys) > 1:
                    lfu_key = next(k for k in self.order if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.frequency[key] = 1

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
