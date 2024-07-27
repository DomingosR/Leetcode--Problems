class Solution(object):
    def getOrder(self, tasks):
        orderedTasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        orderedTasks.sort(reverse = True)

        taskHeap = []
        heapify(taskHeap)
        response = []
        startTime = 0
        
        while taskHeap or orderedTasks:
            if not taskHeap:
                startTime = max(startTime, orderedTasks[-1][0])
            while orderedTasks and orderedTasks[-1][0] <= startTime:
                (_, length, index) = orderedTasks.pop()
                heappush(taskHeap, (length, index))
            (nextLength, nextIndex) = heappop(taskHeap)
            response.append(nextIndex)
            startTime += nextLength

        return response