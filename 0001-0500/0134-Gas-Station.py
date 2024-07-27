class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        netGas = [gas[i] - cost[i] for i in range(n)]
        cumulativeNetGas = list(accumulate(netGas))
        minVal = min(cumulativeNetGas)
        return (cumulativeNetGas.index(minVal) + 1) % n
