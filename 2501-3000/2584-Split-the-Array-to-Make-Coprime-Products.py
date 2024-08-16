maxNum = 10 ** 6
primeFactor = [i for i in range(maxNum + 1)]
for i in range(2, 10 ** 3 + 1):
    if primeFactor[i] == i:
        for j in range(i, maxNum + 1, i):
            primeFactor[j] = i

def getPrimeFactors(num):
    primeFactors = set()
    while num > 1:
        primeFactors.add(primeFactor[num])
        num //= primeFactor[num]
    return primeFactors

class Solution(object):
    def findValidSplit(self, nums):
        if len(nums) == 1:
            return -1
        
        if nums[0] == 1:
            return 0
        
        lastIndex = defaultdict(int)
        
        for i, num in enumerate(nums):
            for p in getPrimeFactors(num):
                lastIndex[p] = i
        
        maxIndex = -1
        for i in range(len(nums) - 1):
            num = nums[i]
            if num == 1:
                continue
                
            for p in getPrimeFactors(num):
                maxIndex = max(maxIndex, lastIndex[p])
            
            if maxIndex == i:
                return i
            
        return -1