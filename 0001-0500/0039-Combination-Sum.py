class Solution(object):
    def combinationSum(self, candidates, target):
        prevCombinations = defaultdict(list)
        prevCombinations[0] = [[]]
        candidates.sort()
        
        def combinations(num):
            if num in prevCombinations:
                return prevCombinations[num]
            
            allCombs = []
            for element in candidates:
                if element <= num:
                    for combination in combinations(num - element):
                        if not combination or combination[0] >= element:
                            allCombs.append([element] + combination)
                
            prevCombinations[num] = allCombs
            return allCombs
        
        return combinations(target)