class Solution(object):
    def sortedSquares(self, nums):
        squares = []
        i, j = 0, len(nums)-1

        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                squares.append(nums[i]*nums[i])
                i += 1
            else:
                squares.append(nums[j]*nums[j])
                j -= 1

        return squares[::-1]
