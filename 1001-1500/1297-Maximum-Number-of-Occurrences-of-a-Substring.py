class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        n = len(s)
        stringCounter = Counter()

        for i in range(n - minSize + 1):
            currentStr = s[i : i + minSize]
            if len(set(currentStr)) <= maxLetters:
                stringCounter[currentStr] += 1
        
        if not stringCounter:
            return 0
            
        return stringCounter.most_common(1)[0][1]