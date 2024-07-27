class Solution(object):
    def knightProbability(self, n, k, row, column):
        stateProb = {(row, column): 1}
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        leaveProb = 0

        for i in range(k):
            nextProb = defaultdict(int)
            for (currentRow, currentCol), currentProb in stateProb.items():
                for move in moves:
                    nextRow, nextCol = currentRow + move[0], currentCol + move[1]
                    if 0 <= nextRow < n and 0 <= nextCol < n:
                        nextProb[(nextRow, nextCol)] += currentProb * 0.125
                    else:
                        leaveProb += currentProb * 0.125
            stateProb = nextProb

        return (1 - leaveProb)
        