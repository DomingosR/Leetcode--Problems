class Solution(object):
    def singleNonDuplicate(self, nums):
        def singleNum(inputList):
            n = len(inputList)
            if n <= 3:
                return sum([inputList[i]*(-1)**i for i in range(n)])

            if inputList[n//2-1] < inputList[n//2] < inputList[n//2+1]:
                return inputList[n//2]

            if n//2 % 2 == 0:
                if inputList[n//2-1] == inputList[n//2]:
                    return singleNum(inputList[:n//2+1])
                else:
                    return singleNum(inputList[n//2:])
            else:
                if inputList[n//2-1] == inputList[n//2]:
                    return singleNum(inputList[n//2+1:])
                else:
                    return singleNum(inputList[:n//2])

        return singleNum(nums)
