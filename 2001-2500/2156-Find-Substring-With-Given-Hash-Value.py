def findDesiredSubstring(s, power, modulo, k, hashValue):
    def val(inputStr):
        return (ord(inputStr[0]) - 96)
    
    strLen = len(s)
    currentHash = 0
    currentMult = 1
    
    for i in range(k):
        currentHash += currentMult * val(s[i])
        if i < k-1:
            currentMult *= power

    nextOrder = k

    while currentHash % modulo != hashValue:
        currentHash = (currentHash - val(s[nextOrder-k])) // power
        currentHash += currentMult * val(s[nextOrder])
        nextOrder += 1

    return s[(nextOrder-k):nextOrder]

class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        return findDesiredSubstring(s, power, modulo, k, hashValue)