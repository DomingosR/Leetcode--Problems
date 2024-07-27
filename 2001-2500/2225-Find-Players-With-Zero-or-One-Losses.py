class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = map(list, zip(*matches))
        noLosses = list(set(winners) - set(losers))
        auxCounter = Counter(losers)
        oneLoss = [player for player in auxCounter.keys() if auxCounter[player] == 1]

        return [sorted(noLosses), sorted(oneLoss)]