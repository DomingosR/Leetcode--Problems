class Solution:
    def robotSim(self, commands, obstacles):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        obstacles = set(map(tuple, obstacles))

        currentX = 0
        currentY = 0
        currentMaxDist = 0
        currentDirIndex = 1 

        for command in commands:
            if command == -2: currentDirIndex = (currentDirIndex + 1) % 4
            if command == -1: currentDirIndex = (currentDirIndex - 1) % 4
            if command > 0:
                numSteps = command
                XStep, YStep = directions[currentDirIndex]
                while numSteps and (currentX + XStep, currentY + YStep) not in obstacles:
                    currentX += XStep
                    currentY += YStep
                    numSteps -= 1
            currentMaxDist = max(currentMaxDist, currentX ** 2 + currentY ** 2)
        
        return currentMaxDist