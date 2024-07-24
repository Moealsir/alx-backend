#!/usr/bin/env python3
""" BasicCache module
"""

from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
