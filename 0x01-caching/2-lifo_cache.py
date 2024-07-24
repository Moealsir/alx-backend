#!/usr/bin/env python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching
OrderedDict = __import__('collections').OrderedDict


class LIFOCache(BaseCaching):
    """ LIFOCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
