class Solution(object):
    def averageWaitingTime(self, customers):
        n, totalWait, finishTime = len(customers), 0, 0
        
        for arrival, duration in customers:
            finishTime = max(finishTime, arrival) + duration
            totalWait += (finishTime - arrival)
        
        return 1.0 * totalWait / n