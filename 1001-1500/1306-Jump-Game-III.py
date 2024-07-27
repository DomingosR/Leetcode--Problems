class Solution(object):
    def canReach(self, nums, start):
        signs = [+1, -1]
        n = len(nums)
        visited = [0] * n

        indexQueue = deque()
        indexQueue.appendleft(start)

        while indexQueue:
            currentIndex = indexQueue.pop()
            if nums[currentIndex] == 0:
                return True
            visited[currentIndex] = 1
            for sign in signs:
                nextIndex = currentIndex + sign * nums[currentIndex]
                if 0 <= nextIndex < n and visited[nextIndex] == 0:
                    indexQueue.appendleft(nextIndex)
        
        return False