class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        n = len(word)
        i = 1
        
        while i * k < n:
            if word[i * k:] == word[ :n-i*k]:
                return i
            i += 1
        
        return i