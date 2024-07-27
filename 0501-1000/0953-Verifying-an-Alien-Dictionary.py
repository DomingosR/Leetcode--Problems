class Solution(object):
    def isAlienSorted(self, words, order):
        letterOrder = {c:i for (i, c) in enumerate(order)}
        adjWords = [[letterOrder[c] for c in word] for word in words]
        auxComp = zip(adjWords[:-1], adjWords[1:])
        return all(currWord <= nextWord for currWord, nextWord in auxComp)
