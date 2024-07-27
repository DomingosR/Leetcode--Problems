class Solution(object):
    def minIncrementForUnique(self, nums):
        parent = defaultdict(int)
        
        def findParent(n):
            parent[n] = findParent(parent[n] + 1) if n in parent else n
            return parent[n]
        
        return sum([findParent(n) - n for n in nums])