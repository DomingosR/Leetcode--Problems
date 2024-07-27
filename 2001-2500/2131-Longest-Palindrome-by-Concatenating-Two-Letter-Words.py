class Solution(object):
    def longestPalindrome(self, words):
        def reverseStr(inputWord):
            return inputWord[::-1]

        maxLength = 0
        identicalUsed = False
        wordCounter = Counter(words)

        for word in wordCounter.keys():
            reversed = reverseStr(word)
            if reversed in wordCounter.keys():
                if word != reversed:
                    while wordCounter[word] > 0 and wordCounter[reversed] > 0:
                        maxLength += 4
                        wordCounter[word] -= 1
                        wordCounter[reversed] -= 1
                else:
                    while wordCounter[word] > 1:
                        maxLength += 4
                        wordCounter[word] -= 2
                    if wordCounter[word] == 1 and identicalUsed == False:
                        maxLength += 2
                        wordCounter[word] -= 1
                        identicalUsed = True

        return maxLength