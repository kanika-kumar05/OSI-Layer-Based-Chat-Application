class RabinKarp:
    def __init__(self, pattern, prime=101):
        self.pattern = pattern
        self.prime = prime
        self.m = len(pattern)
        self.h = pow(256, self.m-1) % self.prime
        self.p_hash = self._hash(pattern)

    def _hash(self, text):
        """Calculate the polynomial rolling hash of a text."""
        h = 0
        for i in range(self.m):
            h = (256 * h + ord(text[i])) % self.prime
        return h

    def search(self, text):
        """Search for the pattern in a text."""
        n = len(text)
        if n < self.m:
            return False

        t_hash = self._hash(text[:self.m])

        for i in range(n - self.m + 1):
            if self.p_hash == t_hash:
                if text[i:i + self.m] == self.pattern:
                    return True

            if i < n - self.m:
                t_hash = (256 * (t_hash - ord(text[i]) * self.h) + ord(text[i + self.m])) % self.prime
                if t_hash < 0:
                    t_hash += self.prime
        return False

# Utility for searching multiple patterns
def contains_patterns(text, patterns):
    for pattern in patterns:
        rk = RabinKarp(pattern)
        if rk.search(text):
            return True
    return False
