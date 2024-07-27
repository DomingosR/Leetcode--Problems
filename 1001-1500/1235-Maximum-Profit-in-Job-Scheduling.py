class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        sortedJobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        profitsByEndTime = [[0, 0]]
        for (start, end, profit) in sortedJobs:
            i = bisect_right(profitsByEndTime, [start + 1]) - 1
            if profitsByEndTime[i][1] + profit > profitsByEndTime[-1][1]:
                profitsByEndTime.append([end, profitsByEndTime[i][1] + profit])
        return profitsByEndTime[-1][1]
        
