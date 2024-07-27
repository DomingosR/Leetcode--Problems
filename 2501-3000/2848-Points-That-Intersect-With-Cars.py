class Solution(object):
    def numberOfPoints(self, nums):
        intervalInfo = nums[0]
        
        for left, right in nums[1:]:
            l = bisect_left(intervalInfo, left)
            r = bisect_right(intervalInfo, right)

            toInsert = []
            if l % 2 == 0: toInsert.append(left)
            if r % 2 == 0: toInsert.append(right)

            intervalInfo[l:r] = toInsert
        
        n = len(intervalInfo) // 2
        
        return sum(intervalInfo[1::2]) - sum(intervalInfo[::2]) + n