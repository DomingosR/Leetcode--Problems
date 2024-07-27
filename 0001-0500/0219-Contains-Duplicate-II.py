class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        indexDictionary = {}

        for i, n in enumerate(nums):
            if n in indexDictionary and i - indexDictionary[n] <= k:
                return True
            indexDictionary[n] = i
            
        return False