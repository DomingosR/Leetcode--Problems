def maxNumUnits(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse = True)
    n = len(boxTypes)      # Number of rows
    m = len(boxTypes[0])   # Number of columns
    totalBoxes = 0
    totalUnits = 0
    row = 0
    
    while totalBoxes < truckSize and row <= n-1:
        boxesToTake = min(truckSize - totalBoxes, boxTypes[row][0])
        totalBoxes += boxesToTake
        totalUnits += boxesToTake * boxTypes[row][1]
        row += 1
    
    return totalUnits

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        return maxNumUnits(boxTypes, truckSize)