class Solution(object):
    def maximumGain(self, s, x, y):
        if x>=y:
            c1, c2, score1, score2 = "a", "b", x, y
        else:
            c1, c2, score1, score2 = "b", "a", y, x
        
        count1, count2, totalScore = 0, 0, 0
        
        for char in s:
            if char == c1:
                count1 += 1
            elif char == c2:
                if count1 > 0:
                    totalScore += score1
                    count1 -= 1
                else:
                    count2 += 1
            else:
                totalScore += min(count1, count2) * score2
                count1 = count2 = 0
              
        totalScore += min(count1, count2) * score2
        
        return totalScore