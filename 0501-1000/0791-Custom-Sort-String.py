class Solution(object):
    def customSortString(self, order, s):
        sSet, sCounter = set(s), Counter(s)
        sortedStr = ""
        
        for char in order:
            sortedStr += char * sCounter[char]
            sSet.discard(char)
            
        for char in list(sSet):
            sortedStr += char * sCounter[char]
            
        return sortedStr