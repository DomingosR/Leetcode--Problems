class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        p = 10**9 + 7
        cities = set(locations)
        startCity = locations[start]
        endCity = locations[finish]

        routeCount = defaultdict(int)

        def countRoutes(currCity, currFuel):
            if currFuel == 0:
                return currCity == endCity

            if (currCity, currFuel) in routeCount:
                return routeCount[(currCity, currFuel)]

            totalCount = 1 if currCity == endCity else 0

            for nextCity in cities:
                if nextCity != currCity and abs(nextCity - currCity) <= currFuel:
                    totalCount += countRoutes(nextCity, currFuel - abs(nextCity - currCity))
            
            routeCount[(currCity, currFuel)] = totalCount
            return totalCount % p

        return countRoutes(startCity, fuel)