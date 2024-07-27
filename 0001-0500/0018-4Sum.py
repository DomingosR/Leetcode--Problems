class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        allQuadruplets = set()
        nums.sort()

        for i in range(n-3):
            for j in range(i+1, n-2):
                adjTarget = target - nums[i] - nums[j]
                k, l = j+1, n-1

                while k < l:
                    if nums[k] + nums[l] < adjTarget:
                        k += 1
                    elif nums[k] + nums[l] > adjTarget:
                        l -= 1
                    else:
                        allQuadruplets.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1

        return allQuadruplets
