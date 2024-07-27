class Solution(object):
    def pivotInteger(self, n):
        auxInt = int(sqrt(n * (n+1) // 2))
        return auxInt if auxInt * auxInt == n * (n + 1) // 2 else -1
