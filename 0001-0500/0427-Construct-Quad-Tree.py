class Solution(object):
    def construct(self, grid):
        def isLeaf(grid):
            return all([grid[i][j] == grid[0][0] for i in range(len(grid)) for j in range(len(grid[i]))])

        def build(grid):
            n = len(grid)

            if isLeaf(grid):
                return Node(grid[0][0] == 1, True, None, None, None, None)

            return Node(True, False,
                build([grid[i][:n//2] for i in range(n//2)]),
                build([grid[i][n//2:] for i in range(n//2)]),
                build([grid[i][:n//2] for i in range(n//2, n)]),
                build([grid[i][n//2:] for i in range(n//2, n)]))

        return build(grid)
