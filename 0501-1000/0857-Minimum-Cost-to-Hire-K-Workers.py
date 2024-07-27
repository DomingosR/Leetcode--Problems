class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        workerInfo = sorted([[1.0 * w / q, q] for w, q in zip(wage, quality)])
        qSum = 1.0 * sum([workerInfo[i][1] for i in range(k)]) 
        minAmount = 1.0 * qSum * workerInfo[k-1][0]
        dataHeap = []
        
        for r, q in workerInfo:
            heappush(dataHeap, -q)
            if len(dataHeap) > k:
                qSum += q
                qSum += heappop(dataHeap)
                minAmount = min(minAmount, 1.0 * qSum * r)
                
        return minAmount