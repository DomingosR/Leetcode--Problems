class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        currentBest = sum(nums[:3])

        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                testSum = nums[i] + nums[j] + nums[k]

                if testSum == target:
                    return target

                if abs(testSum - target) < abs(currentBest - target):
                    currentBest = testSum

                if testSum < target:
                    j += 1

                if testSum > target:
                    k -= 1

        return currentBest
