class Solution(object):
    def getSkyline(self, buildings):
        largeNum = 2 ** 31

        buildings1 = [(leftEnd, -height, rightEnd) for leftEnd, rightEnd, height in buildings]  # Marks start of building
        buildings2 = [(rightEnd, 0, largeNum) for _, rightEnd, _ in buildings]                  # Marks end of building
        buildings3 = buildings1 + buildings2
        buildings3.sort()

        skyLine = [[0, 0]]
        buildingsHeap = [(0, largeNum)]  # Order height (decreasing), then rightEnd (increasing)

        for leftEnd, negHeight, rightEnd in buildings3:
            # Remove buildings that have ended, until we find tallest that has not ended
            while leftEnd >= buildingsHeap[0][1]:
                heapq.heappop(buildingsHeap)

            # If current entry is the start of a new building, enter into heap
            if negHeight:
                heapq.heappush(buildingsHeap, (negHeight, rightEnd))

            # Check if new record is different from current skyLine height, and if so enter into skyLine
            currSkyLineHeight = - buildingsHeap[0][0]
            if skyLine[-1][1] != currSkyLineHeight:
                skyLine.append([leftEnd, currSkyLineHeight])

        # Remove first entry from skyLine before returning
        return skyLine[1:]