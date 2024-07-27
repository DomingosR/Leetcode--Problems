class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        currentList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i in range(n-1):
            nextList = []
            for num in currentList:
                finalDigit = num % 10
                if finalDigit >= k:
                    nextList.append(10 * num + finalDigit - k)
                if k != 0 and finalDigit + k < 10:
                    nextList.append(10 * num + finalDigit + k)
            currentList = nextList

        return currentList
