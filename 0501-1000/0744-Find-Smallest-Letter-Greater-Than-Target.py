class Solution(object):
    def nextGreatestLetter(self, letters, target):
        def findIndexRight(letters, target):
            letterCount = len(letters)

            if target < letters[0]:
                return 0
            if target >= letters[n-1]:
                return letterCount

            lowIndex = 0
            highIndex = letterCount - 1

            while lowIndex < highIndex:
                midIndex = (lowIndex + highIndex) // 2
                if letters[midIndex] <= target:
                    lowIndex = midIndex + 1
                else:
                    highIndex = midIndex

            return lowIndex

        n = len(letters)
        targetIndex = findIndexRight(letters, target)
        return letters[0] if targetIndex == n else letters[targetIndex]
