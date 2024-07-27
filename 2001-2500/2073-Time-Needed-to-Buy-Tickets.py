class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        numUnitsTime = 0

        for i, num in enumerate(tickets):
            if i <= k:
                numUnitsTime += min(tickets[k], tickets[i])
            else:
                numUnitsTime += min(tickets[k] - 1, tickets[i])

        return numUnitsTime
