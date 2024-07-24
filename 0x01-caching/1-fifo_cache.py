#!/usr/bin/env python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching
BaseCaching = __import__('collections').OrderedDict


class FIFOCache(BaseCaching):
    """ FIFOCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
