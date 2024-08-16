class Solution(object):
    def kthDistinct(self, arr, k):
        strCounter = Counter(arr)
        
        for indStr in arr:
            if strCounter[indStr] == 1:
                k -= 1
            if k == 0:
                return indStr
            
        return ""