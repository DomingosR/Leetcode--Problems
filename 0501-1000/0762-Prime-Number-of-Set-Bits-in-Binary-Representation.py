class Solution(object):
    def countPrimeSetBits(self, left, right):
        # Note: the largest power of 2 under 10**6 is 2**19
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        N = sum([2**i for i in primes])

        # Note: below we have:
        # > bin(i).count('1') is the number of ones in the binary representation of i
        # > N >> n shifts the bits in the binary representation of N by n places to the right
        # > Thus, (N >> bin(i).count('1')) & 1 tells whether the [bin(i).count('1') + 1]-th digit of N is 1
        return sum(N >> bin(i).count('1') & 1 for i in range(left, right + 1))
