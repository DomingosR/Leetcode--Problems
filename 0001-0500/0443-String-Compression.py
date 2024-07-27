class Solution(object):
    def compress(self, chars):
        n1 = len(chars)
        outStr = ""
        i = 0

        while i < n1:
            currentChar = chars[i]
            j = i+1
            while j < n1 and chars[j] == currentChar:
                j += 1
            outStr += currentChar
            if j-i > 1:
                outStr += str(j-i)
            i = j

        n2 = len(outStr)
        for i in range(n2):
            chars[i] = outStr[i]

        return n2
