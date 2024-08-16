class Solution(object):
    def minSessions(self, tasks, sessionTime):
        # The idea is to accumulate work sessions in an array
        # and loop through those as we process every task.
        #
        # Credit for the idea for this solution goes to user yo1995
        
        tasks.sort(reverse = True)
        n = len(tasks)
        
        currentSessions = []           # Stores the length of current work sessions
        minSessions = [n]              # Stores the optimal result found so far, can't be more than n
        
        def processTask(taskIndex):
            # If there are more current sessions than the optimal result
            # found so far, no need to proceed.
            if len(currentSessions) >= minSessions[0]:
                return
            
            # If we reached index n, we've managed to fit all tasks into the existing
            # sessions.  By virtue of the previous two lines, this must be the optimal
            # so far.
            if taskIndex == n:
                minSessions[0] = len(currentSessions)
                return
            
            # Otherwise, attempt to fit current task into existing sessions and continue
            for sessionIndex in range(len(currentSessions)):
                if currentSessions[sessionIndex] + tasks[taskIndex] <= sessionTime:
                    currentSessions[sessionIndex] += tasks[taskIndex]
                    processTask(taskIndex + 1)
                    currentSessions[sessionIndex] -= tasks[taskIndex]
                    
            # Finally, try to start a new session with the current task
            currentSessions.append(tasks[taskIndex])
            processTask(taskIndex + 1)
            currentSessions.pop()
        
        # Run the process that will consider all possibilities
        processTask(0)
        
        return minSessions[0]