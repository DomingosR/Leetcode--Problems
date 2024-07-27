class Solution(object):
    def rearrangeCharacters(self, s, target):
        counterS = Counter(s)
        counterT = Counter(target)

        maxNum = len(s)
        for i in counterT.keys():
            maxNum = min(maxNum, counterS[i] // counterT[i])

        return maxNum
