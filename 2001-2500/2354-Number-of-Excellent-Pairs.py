class Solution(object):
    def countExcellentPairs(self, nums, k):
        def bitCount(num):
            count = 0
            while num > 0:
                count += (num & 1)
                num >>= 1
            return count

        inputList = list(set(nums))
        numBits = [bitCount(num) for num in inputList]
        countValues = Counter(numBits)

        totalNum = 0
        for n1 in countValues:
            for n2 in countValues:
                if n1 + n2 >= k:
                    totalNum += countValues[n1] * countValues[n2]

        return totalNum