class Solution(object):
    def findMinMoves(self, machines):
        totalDresses, numMachines = sum(machines), len(machines)
        
        if totalDresses % numMachines:
            return -1
        
        targetNumDresses = totalDresses // numMachines
        minMoves = 0
        netTransferToRight = 0
        
        for machine in machines:
            netTransferToRight = machine + netTransferToRight - targetNumDresses
            minMoves = max(minMoves, abs(netTransferToRight), machine - targetNumDresses)
            
        return minMoves