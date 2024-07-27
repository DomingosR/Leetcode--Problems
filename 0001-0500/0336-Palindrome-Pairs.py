class Solution(object):
    def palindromePairs(self, words):
        wordIndex = {}
        pairs = []

        for i, word in enumerate(words):
            wordIndex[word] = i
            
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                leftPart = word[:j]
                rightPart = word[j:]
                reverseLeft = leftPart[::-1]
                reverseRight = rightPart[::-1]
                
                if reverseLeft in wordIndex and wordIndex[reverseLeft] != i and rightPart == reverseRight:
                    pairs.append([i, wordIndex[reverseLeft]])
                if j != 0 and reverseRight in wordIndex and wordIndex[reverseRight] != i and leftPart == reverseLeft:
                    pairs.append([wordIndex[reverseRight], i])
        
        return pairs