class Solution(object):
    def construct2DArray(self, original, m, n):
        if m * n == len(original):
            finalList, i = [], 0
            while i < len(original):
                finalList.append(original[i:i+n])
                i += n
            return finalList
        return []