class Solution(object):
    def mostFrequent(self, nums, key):
        occurrences = [nums[i+1] for i in range(len(nums)-1) if nums[i] == key]
        targetCounter = Counter(occurrences)
        return targetCounter.most_common(1)[0][0]
