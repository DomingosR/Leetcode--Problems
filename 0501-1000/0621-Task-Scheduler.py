class Solution(object):
    def leastInterval(self, tasks, n):
        numOccurrences = Counter(tasks)
        occurrencesCount = Counter(numOccurrences.values())
        maxCount = max(occurrencesCount.keys())
        numElements = occurrencesCount[maxCount]

        return max(len(tasks), (maxCount - 1) * (n + 1) + numElements)