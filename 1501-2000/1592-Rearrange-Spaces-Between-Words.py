class Solution:
    def reorderSpaces(self, text: str) -> str:
        # First, parse text
        
        allWords = []
        currentIndex = 0
        
        while currentIndex < len(text):
            if text[currentIndex] == " ":
                currentIndex += 1
            else:
                currentWord = ""
                while currentIndex < len(text) and text[currentIndex] != " ":
                    currentWord += text[currentIndex]
                    currentIndex += 1
                allWords.append(currentWord)
                
        totalSpaces = len(text) - sum([len(word) for word in allWords])
        numWords = len(allWords)
        
        if numWords == 1:
            return allWords[0] + " " * totalSpaces
        
        else:
            spacesPerGap = totalSpaces // (numWords - 1)
            
        return (" " * spacesPerGap).join(allWords) + " " * (totalSpaces % (numWords - 1))