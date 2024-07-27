class Solution(object):
    def maxJumps(self, arr, d):
        n = len(arr)
        pathLen = defaultdict()

        def findPathLen(i):
            if i in pathLen:
                return pathLen[i]

            maxPathLen = 0

            for j in range(1, d+1):
                if i+j >= n or arr[i+j] >= arr[i]:
                    break
                maxPathLen = max(findPathLen(i+j), maxPathLen)

            for j in range(1, d+1):
                if i-j < 0 or arr[i-j] >= arr[i]:
                    break
                maxPathLen = max(findPathLen(i-j), maxPathLen)

            pathLen[i] = maxPathLen + 1
            return pathLen[i]

        longestPath = 0
        for i in range(n):
            findPathLen(i)

        return max(pathLen.values())
