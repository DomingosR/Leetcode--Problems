class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        numReq = len(requests)

        for i in range(numReq, 0, -1):
            for comb in combinations(requests, i):
                if Counter(origin for origin, dest in comb) == Counter(dest for origin, dest in comb):
                    return i
                
        return 0
		
class Solution(object):
    def maximumRequests(self, n, requests):
        numReq = len(requests)
        maxFeasible = 0
        
        def numFeasible(k):
            auxList = [[0, 0] for _ in range(n)]
            reqCount = 0
            i = 0
            
            while k > 0:
                if k & 1 == 1:
                    reqCount += 1
                    auxList[requests[i][0]][0] += 1
                    auxList[requests[i][1]][1] += 1
                i += 1
                k >>= 1
            
            return reqCount if all([auxList[j][0] == auxList[j][1] for j in range(n)]) else 0
        
        for k in range(2**numReq):
            maxFeasible = max(maxFeasible, numFeasible(k))
            
        return maxFeasible