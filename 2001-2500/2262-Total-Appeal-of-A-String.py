class Solution(object):
    def appealSum(self, s):
        n = len(s)
        letterIndices = defaultdict(lambda: [-1])
        for i in range(n):
            letterIndices[s[i]].append(i)
        
        returnVal = 0
        for indList in letterIndices.values():
            indList.append(n)
            auxList = [(n - indList[i+1]) * (indList[i+1] - indList[i]) \
                        for i in range(len(indList)-2)]
            returnVal += sum(auxList)

        return returnVal 