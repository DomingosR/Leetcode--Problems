class Solution(object):
    def findPrimePairs(self, n):
        if n <= 3:
            return []

        isPrime = [True] * (n+1)
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(sqrt(n)) + 1):
            if isPrime[i]:
                j = i ** 2
                while j <= n:
                    isPrime[j] = False
                    j += i

        primePairs = []

        for j in range(2, n // 2 + 1):
            if isPrime[j] and isPrime[n-j]:
                primePairs.append([j, n-j])

        return primePairs
