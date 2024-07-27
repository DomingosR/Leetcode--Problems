class Solution(object):
    def createSortedArray(self, instructions):
        maxVal = max(instructions)
        fenTree = [0] * (maxVal + 1)
        
        def update(val):
            while val <= maxVal:
                fenTree[val] += 1
                val += val & (-val)
        
        def get(val):
            count = 0
            while val > 0:
                count += fenTree[val]
                val -= val & (-val)
            return count
                
        numInstructions = 0
        for i, n in enumerate(instructions):
            numInstructions += min(get(n-1), i - get(n))
            update(n)
        
        return numInstructions % (10 ** 9 + 7)