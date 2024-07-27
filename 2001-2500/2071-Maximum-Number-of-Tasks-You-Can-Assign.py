class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        m = len(workers)
        n = len(tasks)

        if m > n:
            workers = workers[m-n:]
        else:
            tasks = tasks[:m]
        
        count = min(m, n)
        auxPills = [pills]
        
        def canAssignNum(k):
            auxWorkers = workers[count-k:]
            auxTasks = tasks[:k]
            auxPills1 = auxPills[0]

            for i in range(k-1, -1, -1):
                if auxWorkers[-1] >= auxTasks[i]:
                    auxWorkers.pop()
                elif auxPills1 > 0:
                    index = bisect_left(auxWorkers, auxTasks[i] - strength)
                    if index == len(auxWorkers):
                        return False
                    else:
                        auxPills1 -= 1
                        auxWorkers.pop(index)
                else:
                    return False
            
            return True
        
        leftVal = 0
        rightVal = count
        
        while leftVal < rightVal:
            midVal = (leftVal + rightVal + 1) // 2
            if canAssignNum(midVal):
                leftVal = midVal
            else:
                rightVal = midVal - 1
                
        return leftVal