class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        workInfo = list(map(list, zip(difficulty, profit)))
        workInfo.sort(key = lambda x: x[0])
        worker.sort()
        
        i, n, totalProfit, maxProfit = -1, len(profit), 0, 0
        
        for j in range(len(worker)):
            while i < n-1 and workInfo[i+1][0] <= worker[j]:
                maxProfit = max(maxProfit, workInfo[i+1][1])
                i += 1
            totalProfit += maxProfit
            
        return totalProfit