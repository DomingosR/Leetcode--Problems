class Solution(object):
    def checkInclusion(self, s1, s2):
        # s2 is the longer string
        n = len(s2)
        m = len(s1)
        refCounter = Counter(s1)
        currCounter = Counter(s2[:m])

        currentIndex = 0

        while currentIndex <= n-m:
            if currCounter == refCounter:
                return True

            if currentIndex < n-m:
                if currCounter[s2[currentIndex]] > 1:
                    currCounter[s2[currentIndex]] -= 1
                else:
                    del currCounter[s2[currentIndex]]
                currCounter[s2[currentIndex + m]] += 1

            currentIndex += 1

        return False
