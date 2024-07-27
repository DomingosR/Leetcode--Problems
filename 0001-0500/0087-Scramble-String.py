class Solution(object):
    checkedPairs = defaultdict()
    
    def isScramble(self, s1, s2):
        if (s1, s2) in self.checkedPairs:
            return self.checkedPairs[(s1, s2)]

        if sorted(s1) != sorted(s2):
            self.checkedPairs[(s1, s2)] = False
            return False

        if s1 == s2:
            self.checkedPairs[(s1, s2)] = True
            return True

        n = len(s1)

        for i in range(1, n):
            left1, right1 = s1[:i], s1[i:]
            left2, right2 = s2[:i], s2[i:]

            if self.isScramble(left1, left2) and self.isScramble(right1, right2):
                self.checkedPairs[(s1, s2)] = True
                return True

            left1, right1 = s1[:n-i], s1[n-i:]

            if self.isScramble(left1, right2) and self.isScramble(left2, right1):
                self.checkedPairs[(s1, s2)] = True
                return True

        self.checkedPairs[(s1, s2)] = False
        return False