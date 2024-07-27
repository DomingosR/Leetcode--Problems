def charVal(letter):
    if letter == "I": return 1
    if letter == "V": return 5
    if letter == "X": return 10
    if letter == "L": return 50
    if letter == "C": return 100
    if letter == "D": return 500
    if letter == "M": return 1000

def romanToInteger(s):
    numChars = len(s)
    numValue = 0
    
    i = 0
    while i < numChars:
        currentVal = charVal(s[i])
        if i < numChars - 1 and charVal(s[i+1]) > charVal(s[i]):
            numValue += charVal(s[i+1]) - charVal(s[i])
            i += 2
        else:
            numValue += charVal(s[i])
            i += 1
    
    return numValue

class Solution(object):
    def romanToInt(self, s):
        return romanToInteger(s)