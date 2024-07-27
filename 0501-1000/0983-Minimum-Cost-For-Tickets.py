class Solution(object):
    def mincostTickets(self, days, costs):
        # Entries in this dictionary will be of the form:
        # i: cost, where cost is the minimum cost for tickets
        # that cover dates days[i:]

        minCost = defaultdict()
        numDays = len(days)

        def lowestCost(i):
            if i >= numDays:
                return 0
            if i in minCost:
                return minCost[i]

            currentDay = days[i]
            index7 = bisect_right(days, currentDay + 6)
            index30 = bisect_right(days, currentDay + 29)

            cost1 = costs[0] + lowestCost(i+1)
            cost7 = costs[1] + lowestCost(index7)
            cost30 = costs[2] + lowestCost(index30)
            returnVal = min(cost1, cost7, cost30)

            minCost[i] = returnVal

            return returnVal

        return lowestCost(0)
