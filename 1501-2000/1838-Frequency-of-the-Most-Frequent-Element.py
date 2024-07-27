class Solution(object):
    def maxFrequency(self, nums, k):
        leftEnd = 0
        nums.sort()
        
        # Intuition:
        #
        # The condition for us to be able to increment all the numbers in 
        # [i, j] to nums[j] is (i - j + 1) * nums[j] <= sum(nums[i:j+1]) + k.  
        # We keep track of the LHS and RHS of this expression.  If the
        # condition holds for a particular value of i and j, we can extend
        # the right end of the interval to see if it still does; otherwise,
        # we extend the left end.
        #
        # Notice that, in the algorithm below, once we find an interval of a
        # certain width satisfying this condition, subsequent intervals of a 
        # lower width are not checked.
        
        RHS = k
        leftEnd = 0
        
        for rightEnd in range(len(nums)):
            RHS += nums[rightEnd]
            LHS = (rightEnd - leftEnd + 1) * nums[rightEnd]
            if RHS < LHS:
                RHS -= nums[leftEnd]
                leftEnd += 1
        return rightEnd - leftEnd + 1   