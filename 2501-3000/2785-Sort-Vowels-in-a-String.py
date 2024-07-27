class Solution(object):
    def sortVowels(self, s):
        vowels = set(["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"])

        strVowels = []
        strConsonants = []
        reorderedStr = ""

        for indChar in s:
            if indChar in vowels:
                strVowels.append(indChar)
            else:
                strConsonants.append(indChar)

        strVowels.sort(key = lambda x: ord(x))
        vowelPtr, consonantPtr = 0, 0

        for indChar in s:
            if indChar in vowels:
                reorderedStr += strVowels[vowelPtr]
                vowelPtr += 1
            else:
                reorderedStr += strConsonants[consonantPtr]
                consonantPtr += 1

        return reorderedStr
