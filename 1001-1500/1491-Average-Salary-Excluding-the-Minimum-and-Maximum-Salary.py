class Solution(object):
    def average(self, salary):
        n = len(salary)
        minVal = min(salary)
        maxVal = max(salary)
        
        return 1.0 * (sum(salary) - minVal - maxVal) / (n - 2)