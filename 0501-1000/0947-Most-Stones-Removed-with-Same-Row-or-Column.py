class Solution(object):
    def removeStones(self, stones):
        stonesToProcess = {(i, j) for i, j in stones}
        components = 0
        colsForRow = collections.defaultdict(list)
        rowsForCol = collections.defaultdict(list)

        for i, j in stones:
            colsForRow[i].append(j)
            rowsForCol[j].append(i)

        def processStone(i, j):
            stonesToProcess.discard((i, j))
            for nextJ in colsForRow[i]:
                if (i, nextJ) in stonesToProcess:
                    processStone(i, nextJ)
            for nextI in rowsForCol[j]:
                if (nextI, j) in stonesToProcess:
                    processStone(nextI, j)

        for i, j in stones:
            if (i, j) in stonesToProcess:
                processStone(i, j)
                components += 1

        return len(stones) - components
