class Solution(object):
    def addBinary(self, a, b):
        if a == "0" and b == "0":
            return "0"

        nA = len(a)
        nB = len(b)
        if nA < nB:
            a, b, nA, nB = b, a, nB, nA

        digitsA = list(map(int, list(a)))[::-1]
        digitsB = list(map(int, list(b)))[::-1]
        result = [0] * (nA + 1)
        
        carry = 0
        for i in range(nA + 1):
            result[i] += carry
            if i < nA:
                result[i] += digitsA[i]
            if i < nB:
                result[i] += digitsB[i]
            carry = 1 if result[i] >= 2 else 0
            result[i] %= 2
        
        sum = "".join([str(result[i]) for i in range(nA, -1, -1)])
        if sum[0] == "0":
            sum = sum[1:]
        
        return sum