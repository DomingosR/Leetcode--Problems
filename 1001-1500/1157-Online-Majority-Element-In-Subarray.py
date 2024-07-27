MAX_NUMBER = 2*10**4
MAX_BIT_COUNT = MAX_NUMBER.bit_length()

class MajorityChecker(object):

    def __init__(self, nums):
        n = len(nums)
        self.bit_sum = [[0] * MAX_BIT_COUNT for _ in range(n+1)]    # Store the sum of bits in the binary representation of
                                                                    # nums[:i] in bit_sum[i+1], so bit_sum[0] = 0
        for i in range(1, n+1):
            for b in range(MAX_BIT_COUNT):
                self.bit_sum[i][b] = self.bit_sum[i-1][b] + ((nums[i-1] >> b) & 1)
                                                                    # This last term gives the b-th bit of nums[i-1] (units bit being 0-th)
        self.numIndices = defaultdict(list)
        for i in range(n):
            self.numIndices[nums[i]].append(i)

    def query(self, left, right, threshold):
        num = 0
        for b in range(MAX_BIT_COUNT):
            if self.bit_sum[right+1][b] - self.bit_sum[left][b] >= threshold:
                num |= (1 << b)                                     # This changes the b-th bit of num from the right into 1 (units bit being 0-th)
        leftEnd = bisect_left(self.numIndices[num], left)
        rightEnd = bisect_right(self.numIndices[num], right)
        if rightEnd - leftEnd >= threshold:
            return num
        return -1
