class Solution(object):
    def beautifulSubsets(self, nums, k):
        numCounters = [Counter() for _ in range(k)]
        
        for num in nums:
            numCounters[num % k][num] += 1
        
        overall = 1
        
        for i in range(k):
            if len(numCounters[i]) > 0:
                values = sorted(list(numCounters[i].keys()))
                inc, exc = 2 ** numCounters[i][values[0]] - 1, 1
                for j in range(1, len(numCounters[i])):
                    if values[j] - values[j-1] == k:
                        inc, exc = (2 ** numCounters[i][values[j]] - 1) * exc, inc + exc
                    else:
                        inc, exc = (2 ** numCounters[i][values[j]] - 1) * (inc + exc), inc + exc

                overall *= (inc + exc)
                      
        return overall - 1