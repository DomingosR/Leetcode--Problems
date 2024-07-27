class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []

        lettersForDigits = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        def combinations(inputStr):
            currentLetters = []
            for c in lettersForDigits[int(inputStr[0])]:
                currentLetters.append(c)

            n = len(inputStr)
            if n == 1:
                return currentLetters
            else:
                previousCombinations = combinations(inputStr[1:])
                return [c + comb for c in currentLetters for comb in previousCombinations]

        return combinations(digits)
