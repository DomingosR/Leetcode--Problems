class Solution(object):
    def minScore(self, n, roads):
        connectedCities = defaultdict(list)
        visited = [False] * (n+1)
        refDist = 10**4 + 1
        
        for city1, city2, dist in roads:
            connectedCities[city1].append((city2, dist))
            connectedCities[city2].append((city1, dist))

        cityQueue = deque()
        cityQueue.appendleft(1)

        while cityQueue:
            currentCity = cityQueue.pop()
            visited[currentCity] = True
            for nextCity, nextDist in connectedCities[currentCity]:
                refDist = min(refDist, nextDist)
                if not visited[nextCity]:
                    cityQueue.appendleft(nextCity)
                
        return refDist