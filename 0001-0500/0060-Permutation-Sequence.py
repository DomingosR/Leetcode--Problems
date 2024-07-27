def permutationK(n, k):
    # Handle trivial case directly
    if n==1:
        return "1"

    factArray = [1 for i in range(n+1)] # i-th entry equals i!
    factArray[0] = 1
    for i in range(1, n+1):
        factArray[i] = i * factArray[i-1]
    intArray = [(i+1) for i in range(n)]

    permutation = ""
    currentNum = k
    order = n

    while order > 0:
        quotient = ((currentNum - 1) // factArray[order - 1])
        permutation += str(intArray[quotient])
        del intArray[quotient]
        currentNum -= quotient * factArray[order - 1]
        order -= 1

    return permutation

class Solution(object):
    def getPermutation(self, n, k):
        return permutationK(n, k)