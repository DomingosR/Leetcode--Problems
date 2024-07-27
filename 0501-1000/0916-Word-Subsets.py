def wordSubset(masterWords, indWords):
    letterCounter = Counter()
    for indWord in indWords:
        letterCounter |= Counter(indWord)

    returnVal = []
    for masterWord in masterWords:
        wordDict = Counter(masterWord)
        if all(wordDict.get(key, 0) >= val for key, val in letterCounter.items()):
            returnVal.append(masterWord)

    return returnVal

class Solution(object):
    def wordSubsets(self, words1, words2):
        return wordSubset(words1, words2)
