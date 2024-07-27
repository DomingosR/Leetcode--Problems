class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def auxFn(i, remainingLetters):
            if i == len(words):
                return 0
            
            currentWord = words[i]
            currentCounter = Counter(currentWord)
            
            if currentCounter <= remainingLetters:
                currentScore = sum([score[ord(letter) - ord("a")] for letter in currentWord])
                return max(currentScore + auxFn(i + 1, remainingLetters - currentCounter), auxFn(i + 1, remainingLetters))
            
            else:
                return auxFn(i + 1, remainingLetters)
        
        return auxFn(0, Counter(letters))        