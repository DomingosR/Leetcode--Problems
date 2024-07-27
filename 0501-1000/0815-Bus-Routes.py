class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        routeNumsForStop = defaultdict(set)
        
        for i, route in enumerate(routes):
            for j in route:
                routeNumsForStop[j].add(i)
                
        seenStops = set([source])
        stopQueue = deque()
        stopQueue.appendleft((source, 0))
        
        while stopQueue:
            currentStop, numBuses = stopQueue.pop()
            if currentStop == target:
                return numBuses
            for routeNum in routeNumsForStop[currentStop]:
                for nextStop in routes[routeNum]:
                    if nextStop not in seenStops:
                        seenStops.add(nextStop)
                        stopQueue.appendleft((nextStop, numBuses + 1))
                routes[routeNum] = []
        
        return -1