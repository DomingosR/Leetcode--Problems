class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        currentWinner = arr[0]
        streak = 0
        
        for i in range(1, len(arr)):
            if arr[i] > currentWinner:
                currentWinner = arr[i]
                streak = 0
            streak += 1
            if streak == k:
                break
        
        return currentWinner