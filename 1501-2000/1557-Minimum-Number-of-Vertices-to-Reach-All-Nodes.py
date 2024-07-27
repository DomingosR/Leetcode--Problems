class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        return list (set(range(n)) - set(list(map(list, zip(*edges)))[1]))