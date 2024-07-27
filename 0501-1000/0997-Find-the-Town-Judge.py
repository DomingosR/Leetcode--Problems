class Solution(object):
    def findJudge(self, n, trust):
        if n == 1:
            return 1
        if not trust:
            return -1

        trustRoles = list(map(list, zip(*trust)))
        trusted = Counter(trustRoles[1])
        possibleJudges = [i for i in trusted.keys() if trusted[i] == n-1]

        if len(possibleJudges) != 1:
            return -1
        if possibleJudges[0] in trustRoles[0]:
            return -1
        return possibleJudges[0]
