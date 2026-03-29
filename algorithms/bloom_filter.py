import hashlib

class BloomFilter:
    def __init__(self, size=1024, hash_count=5):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        """Generate multiple hash values for an item."""
        hashes = []
        for i in range(self.hash_count):
            # Using salt with MD5 to simulate multiple hash functions
            hash_hex = hashlib.md5((str(item) + str(i)).encode()).hexdigest()
            hash_int = int(hash_hex, 16)
            hashes.append(hash_int % self.size)
        return hashes

    def add(self, item):
        """Add an item to the bloom filter."""
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def contains(self, item):
        """Check if an item is likely in the bloom filter."""
        for h in self._hashes(item):
            if self.bit_array[h] == 0:
                return False
        return True
