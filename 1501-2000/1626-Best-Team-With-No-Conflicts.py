class Solution(object):
    def bestTeamScore(self, scores, ages):
        allInfo = list(map(list, zip(ages, scores)))
        # Sort decreasing by age, then decreasing by score
        allInfo.sort(key = lambda x: (-x[0], -x[1]))

        n = len(scores)

        # maxScore will hold the max score of any team that includes only players
        # to the left of that players
        maxScore = [0] * n
        overallMax = 0

        for i in range(n):
            currentScore = allInfo[i][1]
            maxScore[i] = currentScore
            
            for j in range(i):
                # Player j can be selected only if her score is no less than i's
                if allInfo[j][1] >= currentScore:
                    maxScore[i] = max(maxScore[i], maxScore[j] + currentScore)
            overallMax = max(overallMax, maxScore[i])
        
        return overallMax