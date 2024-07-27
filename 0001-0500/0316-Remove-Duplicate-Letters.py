class Solution(object):
    def removeDuplicateLetters(self, s):
        lastOccurrence = {c: i for i, c in enumerate(s)}
        letterStack = []
        inStack = set()

        for i in range(len(s)):
            currentChar = s[i]
            if currentChar in inStack:
                continue
            while letterStack and letterStack[-1] > currentChar and lastOccurrence[letterStack[-1]] > i:
                inStack.remove(letterStack.pop())
            letterStack.append(currentChar)
            inStack.add(currentChar)

        return ''.join(letterStack)
                
