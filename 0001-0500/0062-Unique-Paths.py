def pathCount(m, n):
    total = (m - 1) + (n - 1)
    choose = min(m - 1, n - 1)

    result = 1
    for i in range(choose):
        result = result * (total - i) // (i + 1)

    return result

class Solution(object):
    def uniquePaths(self, m, n):
        return pathCount(m, n)
