class Solution(object):
    def minimumRounds(self, tasks):
        taskLevelCounter = Counter(tasks)

        if 1 in taskLevelCounter.values():
            return -1
        
        return sum([(val + 2) // 3 for val in taskLevelCounter.values()])