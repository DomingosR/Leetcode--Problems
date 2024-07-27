class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)
        rankDict = defaultdict(int)
        adjScore = sorted(score)[::-1]
        rankStr = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, n + 1)))
        rank = [0] * n
        
        for i, num in enumerate(adjScore):
            rankDict[num] = rankStr[i]
            
        for i in range(n):
            rank[i] = rankDict[score[i]]
            
        return rank