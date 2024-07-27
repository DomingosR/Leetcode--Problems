class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay): 
            return -1

        values = sorted(list(set(bloomDay)))
        leftIndex, rightIndex = 0, len(values) - 1

        while  leftIndex < rightIndex:
            midIndex = leftIndex + (rightIndex - leftIndex) // 2
            midVal = values[midIndex]
            currentCount, numBouquets = 0, 0

            for day in bloomDay:
                currentCount = (currentCount + 1 if day <= midVal else 0)
                if currentCount == k:
                    numBouquets += 1
                    if numBouquets == m:
                        break
                    currentCount = 0

            if numBouquets == m:
                rightIndex = midIndex
            else:
                leftIndex = midIndex + 1

        return values[leftIndex]