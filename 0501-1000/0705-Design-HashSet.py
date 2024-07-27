class MyHashSet(object):
    # Using multiplicative hashing:
    #
    #   h(k) = aK mod 2^w / 2^{w-m}, where
    #
    # (1) k is the number we want to hash
    # (2) a is some big odd prime (9718777)
    # (3) m is length in bits of output.  Since there are no more than
    #     10000 operations, 20 works well, as it gives us 1048576 hashes
    # (4) w is size of machine word, in practice any m < w (5 in this case)
    #
    # Credit: user DBabichev.

    def __init__(self):
        self.p = 9718777
        self.hashes = defaultdict(list)

    def computeHash(self, key):
        return ((key * self.p) & (1 << 20) - 1) >> 5

    def add(self, key):
        t = self.computeHash(key)
        if key not in self.hashes[t]:
            self.hashes[t].append(key)

    def remove(self, key):
        t = self.computeHash(key)
        if key in self.hashes[t]:
            self.hashes[t].remove(key)

    def contains(self, key):
        t = self.computeHash(key)
        return key in self.hashes[t]
