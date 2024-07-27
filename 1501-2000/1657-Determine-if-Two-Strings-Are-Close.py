class Solution(object):
    def closeStrings(self, word1, word2):
        return set(word1) == set(word2) and \
            Counter(Counter(word1).values()) == Counter(Counter(word2).values())