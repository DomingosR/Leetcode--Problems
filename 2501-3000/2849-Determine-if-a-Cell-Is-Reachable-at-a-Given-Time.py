class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        maxDist = max(abs(sx - fx), abs(sy - fy))
        return t != 1 if maxDist == 0 else maxDist <= t
