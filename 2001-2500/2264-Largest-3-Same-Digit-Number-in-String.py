class Solution(object):
    def largestGoodInteger(self, num):
        n = len(num)
        results = [str(num[i:i+3]) for i in range(n-2) if num[i] == num[i+1] == num[i+2]] + [""]
        return str(max(results))
