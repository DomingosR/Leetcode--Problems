from collections import defaultdict

def minimumOverallCostV2(houses, cost, m, n, target):
    # The following dictionaries will hold keys with the current color
    # and number of groups up to the current stage
    runningCost = {(0, 0):0}
    currentCost = defaultdict(lambda:float('inf'))

    # Running loop over the houses and respective colors
    for i, h in enumerate(houses):
        # In the loop, prevColor means the previous color and
        # prevGroups the previous number of groups
        for prevColor, prevGroups in runningCost:

            # Check each possible currentColor
            for currentColor in (range(1, n + 1) if not h else [h]):
                
                # If color has changed, number of neighborhoods increases by 1
                currentGroups = prevGroups + (prevColor != currentColor)
                if currentGroups > target: continue

                # Current cost may reduce if painting with currentColor is cheaper than with 
                # any previously tried alternatives
                currentCost[currentColor, currentGroups] = min(currentCost[currentColor, currentGroups], \
                                            runningCost[prevColor, prevGroups]+(cost[i][currentColor-1] \
                                            if currentColor != h else 0))
        
        # Once finished with all possible colors for the current iteration, set runningCost to currentCost
        runningCost = currentCost
        currentCost = defaultdict(lambda:float('inf'))

    return min([runningCost[c, g] for c, g in runningCost if g == target] or [-1])
    
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        return minimumOverallCostV2(houses, cost, m, n, target)