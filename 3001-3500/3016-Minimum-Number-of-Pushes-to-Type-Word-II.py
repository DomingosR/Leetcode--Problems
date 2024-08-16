class Solution(object):
    def minimumPushes(self, word):
        letterCounts = Counter(word).values()
        letterCounts.sort(reverse = True)
        totalPresses, i, multiplier = 0, 0, 1
        
        while i < len(letterCounts):
            totalPresses += letterCounts[i] * multiplier
            i += 1
            if i % 8 == 0:
                multiplier += 1
                
        return totalPresses