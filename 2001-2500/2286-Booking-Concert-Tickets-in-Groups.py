# ***************************************************************
# This implementation will use a segment tree.  The segments in
# the tree nodes cover ranges of seat rows.  In the nodes, we
# we will store the maximum value of free seats in any row in
# the node range and the total number of seats available in the
# range.
# ***************************************************************

class Node(object):
    def __init__(self, startRow, endRow):
        self.start = startRow
        self.end = endRow
        self.left = None
        self.right = None
        self.totalSeats = 0                # Value for range sum
        self.maxSeats = 0                  # Maximum value for single row

class SegmentTree(object):
    def __init__(self, startRow, endRow, value):
        # Auxiliary function to build a subtree of the whole tree
        def buildTree(leftEnd, rightEnd):
            if leftEnd > rightEnd:
                return None

            if leftEnd == rightEnd:
                currentNode = Node(leftEnd, rightEnd)
                currentNode.totalSeats = value
                currentNode.maxSeats = value
                return currentNode

            currentNode = Node(leftEnd, rightEnd)
            middleVal = (leftEnd + rightEnd) // 2
            currentNode.left = buildTree(leftEnd, middleVal)
            currentNode.right = buildTree(middleVal + 1, rightEnd)
            currentNode.maxSeats = max(currentNode.left.maxSeats, currentNode.right.maxSeats)
            currentNode.totalSeats = currentNode.left.totalSeats + currentNode.right.totalSeats

            return currentNode

        # Start initialization by building the root node of the tree
        self.rootNode = buildTree(startRow, endRow)

    # Auxiliary function to update tree with a given value for a given row
    def updateRowValue(self, rowIndex, val):
        # Recursive function to do the update starting at a single node
        def updateAux(currentNode):
            if currentNode.start == currentNode.end == rowIndex:
                currentNode.totalSeats -= val
                currentNode.maxSeats -= val
                return

            middleVal = (currentNode.start + currentNode.end) // 2
            if rowIndex <= middleVal:
                updateAux(currentNode.left)
            elif rowIndex > middleVal:
                updateAux(currentNode.right)

            currentNode.maxSeats = max(currentNode.left.maxSeats, currentNode.right.maxSeats)
            currentNode.totalSeats = currentNode.left.totalSeats + currentNode.right.totalSeats
            return

        # Start recursion at the root node of the tree
        updateAux(self.rootNode)

    # Function to perform a maximum query in a given interval
    # Note: the argument seats corresponds to the number of seats in each row,
    #       that is, the m of the problem
    def maxValueQuery(self, k, maxRow, seats):
        # Recursive function to do the query at a single node
        def maxQueryAux(currentNode):
            # Process node if it corresponds to a single row
            if currentNode.start == currentNode.end:
                # Check if the row number is in the valid range and if
                # there are enough seats left in it
                if currentNode.end > maxRow or currentNode.totalSeats < k:
                    return []
                if currentNode.end <= maxRow and currentNode.totalSeats >= k:
                    # The second element below equals m - (occupied seats in row)
                    return [currentNode.end, seats - currentNode.totalSeats]

            # Otherwise, greedily search tree starting from the left
            if currentNode.left.maxSeats >= k:
                return maxQueryAux(currentNode.left)
            return maxQueryAux(currentNode.right)

        # Start query at the root node of the tree
        return maxQueryAux(self.rootNode)

    # Function to perform a total value query in a given interval
    def totalValueQuery(self, maxRow):
        # Recursive function to do the query at a single node
        # This returns the total number of empty seats in the intersection
        # of the interval covered by the current node and the interval
        # [leftEnd, rightEnd]
        def totalQueryAux(currentNode, leftEnd, rightEnd):
            if leftEnd <= currentNode.start and currentNode.end <= rightEnd:
                return currentNode.totalSeats

            middleVal = (currentNode.start + currentNode.end) // 2
            if rightEnd <= middleVal:
                return totalQueryAux(currentNode.left, leftEnd, rightEnd)
            elif leftEnd > middleVal:
                return totalQueryAux(currentNode.right, leftEnd, rightEnd)

            auxVal = totalQueryAux(currentNode.left, leftEnd, middleVal)
            auxVal += totalQueryAux(currentNode.right, middleVal + 1, rightEnd)

            return auxVal

        return totalQueryAux(self.rootNode, 0, maxRow)

class BookMyShow(object):
    def __init__(self, n, m):
        self.m = m
        self.segTree = SegmentTree(0, n-1, m)
        self.freeSeats = [m] * n               # Number of free seats per row
        self.startRow = 0                      # First row with free seats

    def gather(self, k, maxRow):
        res = self.segTree.maxValueQuery(k, maxRow, self.m)

        # If there is a response to maxValueQuery, seats were found, so we need
        # to update the tree accordingly
        if res:
            row = res[0]
            self.segTree.updateRowValue(row, k)
            self.freeSeats[row] -= k

        return res

    def scatter(self, k, maxRow):
        if self.segTree.totalValueQuery(maxRow) < k:
            return False
        else:
            i = self.startRow
            total = 0
            while total < k:
                previousTotal = total
                total += self.freeSeats[i]
                if total < k:
                    self.segTree.updateRowValue(i, self.freeSeats[i])
                    self.freeSeats[i] = 0
                    i += 1
                    self.startRow = i
                elif total >= k:
                    self.segTree.updateRowValue(i, k - previousTotal)
                    self.freeSeats[i] -= (k - previousTotal)

            return True