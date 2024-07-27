class Solution(object):
    def numberOfSubarrays(self, nums, k):
		i = 0
		currentCount = 0
		numArrays = 0
		
		for j in range(len(nums)):
			if nums[j] % 2:
				k -= 1
				currentCount = 0
			while k == 0:
				k += (nums[i] % 2)
				i += 1
				currentCount += 1
			numArrays += currentCount
			
		return numArrays