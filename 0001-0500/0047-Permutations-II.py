class Solution(object):
    def permuteUnique(self, nums):
        n = len(nums)
        numsCounter = Counter(nums)
        allPerms = []
        
        def processPath(currentPath):
            if len(currentPath) == n:
                allPerms.append(currentPath)
                return
            
            for u in numsCounter:
                if numsCounter[u] > 0:
                    numsCounter[u] -= 1
                    processPath(currentPath + [u])
                    numsCounter[u] += 1
                    
        processPath([])
        return allPerms
        