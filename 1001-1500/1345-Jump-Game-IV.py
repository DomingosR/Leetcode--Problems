class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        visited = set()
        valueIndices = defaultdict(list)

        for i, val in enumerate(arr):
            valueIndices[val].append(i)

        indexQueue = deque()
        indexQueue.appendleft((0, 0))
        visited.add(0)

        while indexQueue:
            currentIndex, currentSteps = indexQueue.pop()
            if currentIndex == n-1:
                return currentSteps
            currentVal = arr[currentIndex]
            for nextIndex in [currentIndex-1, currentIndex+1] + valueIndices[currentVal]:
                if 0 <= nextIndex <= n-1 and nextIndex not in visited:
                    indexQueue.appendleft((nextIndex, currentSteps + 1))
                    visited.add(nextIndex)
            valueIndices[currentVal] = []

        return -1
