class Solution(object):
    def increasingTriplet(self, nums):
        auxNum1 = float('inf')
        auxNum2 = float('inf')

        for num in nums:
            if num <= auxNum1:
                auxNum1 = num
            elif num <= auxNum2:
                auxNum2 = num
            else:
                return True

        return False
