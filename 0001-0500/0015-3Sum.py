class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        validTriplets = []

        if n <= 2:
            return validTriplets

        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum < 0:
                    j +=1
                elif currentSum > 0:
                    k -= 1
                else:
                    validTriplets.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1

        return validTriplets
