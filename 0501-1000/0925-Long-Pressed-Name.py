class Solution(object):
    def isLongPressedName(self, name, typed):
        i, j = 0, 0
        
        while i < len(name) and j < len(typed):
            nameChar = name[i]
            typedChar = typed[j]
            if nameChar != typedChar:
                return False
            
            nameCount, typedCount = 0, 0
            while i < len(name) and name[i] == nameChar:
                nameCount += 1
                i += 1
            while j < len(typed) and typed[j] == typedChar:
                typedCount += 1
                j += 1
            if nameCount > typedCount:
                return False
            
        return (i == len(name) and j == len(typed))