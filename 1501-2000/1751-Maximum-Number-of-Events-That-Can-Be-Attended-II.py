class Solution(object):
    def maxValue(self, events, k):
        events.sort(key = lambda x: x[1])
        
        maxVal, auxMaxVal = [[0, 0]], [[0, 0]]
        for i in range(k):
            for start, end, value in events:
                # Find last end time before beginning of current events
                i = bisect.bisect(maxVal, [start]) - 1
                
                # Add event if it increases maximum value
                if maxVal[i][1] + value > auxMaxVal[-1][1]:
                    auxMaxVal.append([end, maxVal[i][1] + value])
                    
            maxVal, auxMaxVal = auxMaxVal, [[0, 0]]
            
        return maxVal[-1][-1]