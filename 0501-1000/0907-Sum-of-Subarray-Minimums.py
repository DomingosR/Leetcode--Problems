class Solution(object):
    def sumSubarrayMins(self, arr):
        p = 10**9 + 7

        n = len(arr)
        prevLower = [-1] * n
        nextLower = [n] * n
        currentStack = []

        for i in range(n):
            while currentStack and arr[currentStack[-1]] > arr[i]:
                j = currentStack[-1]
                nextLower[j] = i
                currentStack.pop()
            if currentStack:
                prevLower[i] = currentStack[-1]
            currentStack.append(i)

        return (sum([arr[i] * (i - prevLower[i]) * (nextLower[i] - i) for i in range(n)]) % p)
