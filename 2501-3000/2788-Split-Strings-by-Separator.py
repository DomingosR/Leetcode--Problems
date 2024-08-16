class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        allWords = []
        
        for word in words:
            allWords += word.split(separator)
        
        allWords = [word for word in allWords if word != ""]
        return allWords