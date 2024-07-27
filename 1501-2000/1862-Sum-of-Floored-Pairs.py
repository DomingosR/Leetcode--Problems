p = 1000000007

def floorSum(nums):
    frequency = Counter(nums)
    maxNum = max(nums)
    auxArray = [0] * (maxNum + 1)

    for key in frequency:
        currentNum = frequency[key]
        multiplier = 1
        while multiplier * key <= maxNum:
            auxArray[multiplier * key] += currentNum
            multiplier += 1

    count = 0
    total = 0
    for i in range(len(auxArray)):
        count += auxArray[i]
        if i in frequency:
            total += frequency[i] * count
    
    return total % p

class Solution(object):
    def sumOfFlooredPairs(self, nums):
        return floorSum(nums)