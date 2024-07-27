class Solution(object):
    def detectCapitalUse(self, word):
        n = len(word)
        if n == 1:
            return True
        
        firstIsCapital = 1 if ord(word[0]) <= ord('Z') else 0
        charCodes = [ord(word[i]) for i in range(1, n)]

        if min(charCodes) >= ord('a'):                        # All characters other than first are lowercase
            return True

        if max(charCodes) <= ord('Z') and firstIsCapital:     # All characters other than first are uppercase
            return True
        
        return False