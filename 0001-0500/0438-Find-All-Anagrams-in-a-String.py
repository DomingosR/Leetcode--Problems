class Solution(object):
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)
        refCounter = Counter(p)
        currCounter = Counter(s[:m])
        currentIndex = 0

        validIndices = []

        while currentIndex <= n-m:
            if currCounter == refCounter:
                validIndices.append(currentIndex)

            if currentIndex < n-m:
                if currCounter[s[currentIndex]] > 1:
                    currCounter[s[currentIndex]] -= 1
                else:
                    del currCounter[s[currentIndex]]
                currCounter[s[currentIndex + m]] += 1

            currentIndex += 1

        return validIndices
