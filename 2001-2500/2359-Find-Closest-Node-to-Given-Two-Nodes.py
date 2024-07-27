class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        n = len(edges)
        distFrom1 = [n] * n
        distFrom2 = [n] * n

        currentDist = 0
        while node1 != -1 and distFrom1[node1] == n:
            distFrom1[node1] = currentDist
            currentDist += 1
            node1 = edges[node1]
        print(distFrom1)

        currentDist = 0
        while node2 != -1 and distFrom2[node2] == n:
            distFrom2[node2] = currentDist
            currentDist += 1
            node2 = edges[node2]
        print(distFrom2)

        minDist = n
        minDistNode = -1

        for i in range(n):
            if max(distFrom1[i], distFrom2[i]) < minDist:
                minDist = max(distFrom1[i], distFrom2[i])
                minDistNode = i
        
        return minDistNode