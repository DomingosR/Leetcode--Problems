class Solution(object):
    def largestMerge(self, word1, word2):
        if word1 >= word2 and word2 > "":
            return word1[0] + self.largestMerge(word1[1:], word2)
        if word2 >= word1 and word1 > "":
            return word2[0] + self.largestMerge(word1, word2[1:])
        return word1 + word2