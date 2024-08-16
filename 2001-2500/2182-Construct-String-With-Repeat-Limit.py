class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        letterCount = [0] * 26
        baseline = ord('a')
        
        for letter in s:
            letterCount[ord(letter) - baseline] += 1
            
        repeatStr, i = "", 25
        
        while i >= 0:
            if letterCount[i] == 0 or (repeatStr and repeatStr[-1] == chr(baseline + i)):
                i -= 1
                continue
            
            j = i-1
            while letterCount[i] > 0:
                for _ in range(min(letterCount[i], repeatLimit)):
                    repeatStr += chr(baseline + i)
                    letterCount[i] -= 1
                    
                if letterCount[i] > 0:
                    while j >= 0:
                        if letterCount[j] > 0:
                            repeatStr += chr(baseline + j)
                            letterCount[j] -= 1
                            break
                        j -= 1
                        
                if j < 0:
                    break
                    
        return repeatStr