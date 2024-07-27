def canJumpAcross(stones):
    numStones = len(stones)
    if numStones <= 1:
        return True
    
    if numStones == 2:
        if stones[1] - stones[0] == 1:
            return True
        else:
            return False
    
    if stones[1] - stones[0] != 1:
        return False
    
    maxStone = stones[-1]
    winningJumps = [set() for i in range(numStones)]

    def addToWinningJumps(i, j):
        jump = stones[j] - stones[i]
        if jump in winningJumps[j] or j == numStones - 1:
            winningJumps[i].add(jump)
            winningJumps[i].add(jump + 1)
            if jump >= 2:
                winningJumps[i].add(jump - 1)

    i = numStones - 2
    while i > 0:
        for j in range(i+1, numStones):
            addToWinningJumps(i, j)
        i -= 1

    return 1 in winningJumps[1]

class Solution(object):
    def canCross(self, stones):
        return canJumpAcross(stones)