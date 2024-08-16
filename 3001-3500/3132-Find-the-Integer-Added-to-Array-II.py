class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        nums1.sort()
        counter2, max2 = Counter(nums2), max(nums2)
        
        for i in range(1, 3):
            counter1 = Counter([num + (max2 - nums1[-i]) for num in nums1])
            if all([counter1[val] - counter2[val] >= 0 for val in counter2]):
                return max2 - nums1[-i]
            
        return max2 - nums1[-3]