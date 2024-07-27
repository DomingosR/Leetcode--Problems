class Solution(object):
    def sortPeople(self, names, heights):
        allInfo = list(map(list, zip(names, heights)))
        allInfo.sort(key = lambda x: -x[1])
        return [allInfo[i][0] for i in range(len(names))]