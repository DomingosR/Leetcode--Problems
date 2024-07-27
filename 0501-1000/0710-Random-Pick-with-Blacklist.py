class Solution(object):

    def __init__(self, n, blacklist):
        blacklist.sort()
        self.blacklisted = set(blacklist)
        self.mapping = {}
        self.numCount = n - len(blacklist)
        
        i = 0
        for j in range(self.numCount, n):
            if j not in self.blacklisted:
                self.mapping[blacklist[i]] = j
                i += 1

    def pick(self):
        i = randint(0, self.numCount - 1)
        return self.mapping[i] if i in self.blacklisted else i