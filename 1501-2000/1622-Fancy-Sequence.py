class Fancy(object):
    def __init__(self):
        self.p = 1000000007
        self.inv = [None] + [pow(m, -1, self.p) for m in range(1, 101)]
        self.fancy = []
        self.a = 1
        self.ainv = 1
        self.b = 0

    def append(self, val):
        self.fancy.append((val - self.b) * self.ainv)

    def addAll(self, inc):
        self.b = (self.b + inc) % self.p
        
    def multAll(self, m):
        self.a = (self.a * m) % self.p
        self.ainv = (self.ainv * self.inv[m]) % self.p
        self.b = (self.b * m) % self.p
        
    def getIndex(self, idx):
        if idx >= len(self.fancy):
            return -1
        tempVal = (self.a * self.fancy[idx] + self.b) % self.p
        return tempVal

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)