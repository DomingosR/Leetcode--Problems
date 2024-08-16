class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        allCombs = []
        
        def processNumber(i, currentPath, currentSum):
            if currentSum > target:
                return
            
            if currentSum == target:
                allCombs.append(currentPath)
                
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                processNumber(j+1, currentPath + [candidates[j]], currentSum + candidates[j])
                
        processNumber(0, [], 0)
        return allCombs
        