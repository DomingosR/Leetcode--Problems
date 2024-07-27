class Solution(object):
    def reverseWords(self, s):
        splitString = s.split()
        reversed = ""

        for i in range(len(splitString) - 1, -1, -1):
            reversed += splitString[i]
            if i > 0:
                reversed += " "
        
        return reversed