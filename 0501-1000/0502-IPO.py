class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        # Heap to include only possible projects, with required
        # capital that does not exceed available one
        possibleProjects = []

        # Combine profits and capital, sorted by capita
        allProjects = sorted(zip(profits, capital), key = lambda x: x[1])

        nextAvailable = 0
        for _ in range(k):
            # Add possible projects to heap
            while nextAvailable < len(allProjects) and allProjects[nextAvailable][1] <= w:
                heapq.heappush(possibleProjects, -allProjects[nextAvailable][0])
                nextAvailable += 1
            # Carry out most profitable project
            if possibleProjects:
                w -= heapq.heappop(possibleProjects)

        return w