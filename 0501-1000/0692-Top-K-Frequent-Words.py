class Solution(object):
    def topKFrequent(self, words, k):
        wordCounter = Counter(words)
        sortedCounter = sorted(wordCounter.items(), key = lambda x:(-x[1], x[0]))
        return [x[0] for x in sortedCounter[:k]]