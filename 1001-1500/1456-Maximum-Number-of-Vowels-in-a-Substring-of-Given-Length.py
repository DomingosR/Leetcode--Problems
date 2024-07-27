class Solution(object):
    def maxVowels(self, s, k):
        vowels = {"a", "e", "i", "o", "u"}
        currentCount = 0
        maxCount = 0

        for i in range(len(s)):
            if s[i] in vowels:
                currentCount += 1
            if i >= k and s[i-k] in vowels:
                currentCount -= 1
            maxCount = max(maxCount, currentCount)

        return maxCount
