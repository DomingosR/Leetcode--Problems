class Solution(object):
    def removeKdigits(self, nums, k):
        digitStack = []
        n = len(nums)

        if n == k:
            return "0"

        for i in range(n):
            while (k > 0) and digitStack and (digitStack[-1] > nums[i]):
                digitStack.pop()
                k -= 1
            digitStack.append(nums[i])

        while k > 0:
            digitStack.pop()
            k -= 1

        auxStr = "".join(digitStack).lstrip("0")

        if auxStr == "":
            return "0"
        else:
            return auxStr
