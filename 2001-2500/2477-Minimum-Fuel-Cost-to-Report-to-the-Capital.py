class Solution(object):
    def minimumFuelCost(self, roads, seats):
        numCities = len(roads) + 1
        connectedCities = defaultdict(list)
        for city1, city2 in roads:
            connectedCities[city1].append(city2)
            connectedCities[city2].append(city1)

        numTravelers = [0] * numCities

        def dfs(currentCity):
            travelers = 1
            for nextCity in connectedCities[currentCity]:
                connectedCities[nextCity].remove(currentCity)
                travelers += dfs(nextCity)
            connectedCities[currentCity] = []
            numTravelers[currentCity] = travelers
            return travelers
        
        dfs(0)

        return sum([(numTravelers[i] + seats - 1) // seats for i in range(1, numCities)])