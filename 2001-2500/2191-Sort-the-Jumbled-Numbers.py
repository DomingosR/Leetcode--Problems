class Solution(object):
    def sortJumbled(self, mapping, nums):
        def mappedVal(num):
            numStr = str(num)
            mappedStr = ""
            
            for i in range(len(numStr)):
                mappedStr += str(mapping[int(numStr[i])])
                
            return int(mappedStr)
        
        auxNums = [(nums[i], i) for i in range(len(nums))]
        auxNums.sort(key = lambda x: (mappedVal(x[0]), x[1]))
        return [x[0] for x in auxNums]