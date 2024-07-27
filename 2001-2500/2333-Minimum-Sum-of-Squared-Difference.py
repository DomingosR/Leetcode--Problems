class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffArray = [abs(nums1[i] - nums2[i]) for i in range(len(nums1)) if nums1[i] != nums2[i]]
        diffCounterAux = Counter(diffArray)
        diffCounter = sorted(diffCounterAux.items(), key = lambda x: x[0])
        diffCounter = [(0, len(nums1))] + diffCounter
        diffCounterList = [[diffCounter[i][0], diffCounter[i][1]] for i in range(len(diffCounter))]

        k = k1 + k2
        i = len(diffCounterList) - 1

        while i >= 1 and k > 0:
            lastVal, lastFreq = diffCounterList[i]
            prevVal = diffCounter[i-1][0]
            if (lastVal - prevVal) * lastFreq < k:
                diffCounterList[i-1][1] += lastFreq
                k -= (lastVal - prevVal) * lastFreq
                i -= 1
                diffCounterList.pop()
            else:
                quotient = k // lastFreq
                remainder = k % lastFreq
                pair1 = (lastVal - quotient - 1, remainder)
                pair2 = (lastVal - quotient, lastFreq - remainder)
                diffCounterList.pop()
                diffCounterList.extend([pair1, pair2])
                k = 0

        return sum([diffCounterList[i][1] * diffCounterList[i][0]**2 for i in range(len(diffCounterList))])