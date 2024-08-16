class Solution(object):
    def finalValueAfterOperations(self, operations):
        finalVal = 0
        incrementOps = ["++X", "X++"]
        for operation in operations:
            finalVal += (1 if operation in incrementOps else -1)
        return finalVal