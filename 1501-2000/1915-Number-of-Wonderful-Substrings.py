class Solution(object):
    def wonderfulSubstrings(self, word):
        numSubstrings = 0
        prefixCount = [1] + [0] * 1023
        currentPrefix = 0
        
        for char in word:
            i = ord(char) - ord("a")
            currentPrefix ^= (1 << i)
            numSubstrings += prefixCount[currentPrefix]
            numSubstrings += sum([prefixCount[currentPrefix ^ (1 << j)] for j in range(10)])
            prefixCount[currentPrefix] += 1
        
        return numSubstrings