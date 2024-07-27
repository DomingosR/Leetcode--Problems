class Solution(object):
    def numMatchingSubseq(self, s, words):
        def isSubsequence(word):
            currentIndex = 0
            for i in range(len(word)):
                currentIndex = s.find(word[i], currentIndex) + 1
                if currentIndex == 0:
                    return False
            
            return True

        subseqCount = 0

        for word in words:
            if isSubsequence(word):
                subseqCount += 1

        return subseqCount