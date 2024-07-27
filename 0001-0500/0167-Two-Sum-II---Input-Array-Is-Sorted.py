class Solution(object):
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        
        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1