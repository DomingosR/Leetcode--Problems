class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        currentIndex = 0
        
        for i in range(1, target[-1] + 1):
            operations.append("Push")
            if target[currentIndex] == i:
                currentIndex += 1
            else:
                operations.append("Pop")
            
        return operations
        