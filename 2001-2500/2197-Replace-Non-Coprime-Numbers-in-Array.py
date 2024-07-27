def gcd(a, b):
    if b > a:
        temp = a
        a = b
        b = temp
        
    while (a % b != 0):
        temp = a % b
        a = b
        b = temp
    
    return b

def adjustedArray(inputArray):
    stack = []

    for n in inputArray:
        while (stack and gcd(n, stack[-1]) > 1):
            auxNum = stack.pop()
            n = int(n * auxNum /gcd(n, auxNum))
        stack.append(n)

    return stack

class Solution(object):
    def replaceNonCoprimes(self, nums):
        return adjustedArray(nums)