class Solution(object):
    def checkIfPangram(self, sentence):
        letterCounter = Counter(sentence)
        return len(letterCounter.items()) == 26
