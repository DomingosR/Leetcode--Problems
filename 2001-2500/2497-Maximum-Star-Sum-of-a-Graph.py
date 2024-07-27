class Solution(object):
    def maxStarSum(self, vals, edges, k):
        n = len(vals)
        adjacentNodes = defaultdict(list)

        for v1, v2 in edges:
            adjacentNodes[v1].append(v2)
            adjacentNodes[v2].append(v1)

        maxVal = -10**4 - 1

        for i in range(n):
            currentVal = vals[i]
            adjacentVals = [vals[j] for j in adjacentNodes[i]]
            adjacentVals.sort(reverse = True)
            j = 0
            while j < min(k, len(adjacentVals)) and adjacentVals[j] > 0:
                currentVal += adjacentVals[j]
                j += 1
            maxVal = max(maxVal, currentVal)

        return maxVal
