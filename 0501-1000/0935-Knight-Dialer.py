class Solution(object):
    def knightDialer(self, n):
        if n == 1:
            return 10

        moves = [[1, 6], [1, 8], [2, 7], [2, 9], [3, 4], [3, 8], [4, 9], [4, 0], [6, 7], [6, 0]]
        adjacent = defaultdict(set)
        sequences = defaultdict(int)
        for i in range(10):
            sequences[(i, 0)] = 1

        for v1, v2 in moves:
            adjacent[v1].add(v2)
            adjacent[v2].add(v1)

        for numMoves in range(1, n):
            for i in range(10):
                for j in adjacent[i]:
                    sequences[(i, numMoves)] += sequences[(j, numMoves-1)]

        return sum([sequences[(i, n-1)] for i in range(10)]) % (10**9 + 7)
