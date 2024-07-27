class Solution(object):
    def removeStars(self, s):
        letters = []

        for i in range(len(s)):
            if s[i] == "*":
                letters.pop()
            else:
                letters.append(s[i])
        
        return "".join(letters)