class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)

        if n <= 2:
            return n

        numFruits = 2
        leftPointer = 0
        typeCounter = Counter(fruits[:2])

        for rightPointer in range(2, n):
            if len(typeCounter) < 2 or fruits[rightPointer] in typeCounter:
                typeCounter[fruits[rightPointer]] += 1
            else:
                typeCounter[fruits[rightPointer]] = 1
                while typeCounter[fruits[leftPointer]] > 1:
                    typeCounter[fruits[leftPointer]] -= 1
                    leftPointer += 1
                del typeCounter[fruits[leftPointer]]
                leftPointer += 1
            numFruits = max(numFruits, rightPointer - leftPointer + 1)

        return numFruits
