class Solution(object):
    def eliminateMaximum(self, dist, speed):
        n = len(dist)
        arrival = [dist[i] // speed[i] + (0 if dist[i] % speed[i] == 0 else 1) for i in range(n)]
        arrival.sort()
        for i, t in enumerate(arrival):
            if t <= i:
                return t
        return n