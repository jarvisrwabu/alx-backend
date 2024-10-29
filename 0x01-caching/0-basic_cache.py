#!/usr/bin/env python3
"""Basic cache class."""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic cache."""

    def __init__(self):
        """Inherit init from parent class."""
        super().__init__()

    def put(self, key, item):
        """Add cache as a key value pair."""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get value associaated to ak key."""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
