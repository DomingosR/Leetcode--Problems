class Solution(object):
    def arrangeWords(self, text):
        words = text.split(" ")
        wordInfo = [(words[i].lower(), i) for i in range(len(words))]
        wordInfo.sort(key = lambda x: (len(x[0]), x[1]))
        reorderedWords = [pair[0] for pair in wordInfo]
        finalStr = " ".join(reorderedWords)
        finalStr = finalStr[:1].upper() + finalStr[1:]
        
        return finalStr