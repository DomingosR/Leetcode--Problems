class Solution(object):
    def maximumDetonation(self, bombs):
        n = len(bombs)
        secondaryBombs = defaultdict(list)

        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(i + 1, n):
                xj, yj, rj = bombs[j]
                distSq = (xi - xj) ** 2 + (yi - yj) ** 2
                if distSq <= ri ** 2:
                    secondaryBombs[i].append(j)
                if distSq <= rj ** 2:
                    secondaryBombs[j].append(i)
        
        maxBombs = 0

        for i in range(n):
            seen = [0] * n
            seen[i] = 1
            numBombs = 1
            queue = deque()
            queue.appendleft(i)

            while queue:
                thisBomb = queue.pop()
                for j in secondaryBombs[thisBomb]:
                    if seen[j] == 0:
                        seen[j] = 1
                        queue.appendleft(j)
                        numBombs += 1
            
            maxBombs = max(maxBombs, numBombs)

        return maxBombs