from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        avgLevels = [root.val]
        processingQueue = deque()

        if root.left != None:
            processingQueue.appendleft((root.left, 1))
        if root.right != None:
            processingQueue.appendleft((root.right, 1))
        
        currentLevel = 1
        currentSum = 0
        currentCount = 0
        
        while processingQueue:
            toProcess = processingQueue.pop()
            nodeToProcess = toProcess[0]
            nodeLevel = toProcess[1]
            
            if nodeLevel > currentLevel:
                avgVal = float(currentSum) / float(currentCount)
                avgLevels.append(avgVal)
                currentLevel = nodeLevel
                currentSum = nodeToProcess.val
                currentCount = 1
            else:
                currentSum += nodeToProcess.val
                currentCount += 1
            
            if nodeToProcess.left != None:
                processingQueue.appendleft((nodeToProcess.left, nodeLevel + 1))
            if nodeToProcess.right != None:
                processingQueue.appendleft((nodeToProcess.right, nodeLevel + 1))
        
        if currentLevel > 0 and currentCount > 0:
            avgVal = float(currentSum) / float(currentCount)
            avgLevels.append(avgVal) 
        
        return avgLevels