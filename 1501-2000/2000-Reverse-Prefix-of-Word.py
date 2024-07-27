class Solution(object):
    def reversePrefix(self, word, ch):
        i = word.find(ch)
        return word if i == -1 else word[:i+1][::-1] + word[i+1:]
