class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        existingWords = set(words)
        seenWords = {}
        concatenatedWords = []

        def isConcatenated(word):
            if word in seenWords:
                return seenWords[word]
                
            seenWords[word] = False

            for i in range(1, len(word)):
                leftPart = word[:i]
                rightPart = word[i:]

                if leftPart in existingWords and rightPart in existingWords:
                    seenWords[word] = True
                    break

                if leftPart in existingWords and isConcatenated(rightPart):
                    seenWords[word] = True
                    break

                if isConcatenated(leftPart) and rightPart in existingWords:
                    seenWords[word] = True
                    break
                
            return seenWords[word]

        for word in existingWords:
            if isConcatenated(word):
                concatenatedWords.append(word)
        
        return concatenatedWords