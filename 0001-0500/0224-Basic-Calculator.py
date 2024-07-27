class Solution(object):
    def calculate(self, s):
        s.replace(" ","")
        
        prevNum = [0]
        prevSign = [1]
        currentNum = 0
        
        for i in s + "+":
            if i.isdigit():
                currentNum = 10 * currentNum + int(i)
            if i in {"+", "-"}:
                prevNum[-1] += prevSign[-1] * currentNum
                prevSign[-1] = (1 if i=="+" else -1)
                currentNum = 0
            if i == "(":
                prevNum.append(0)
                prevSign.append(1)
                currentNum = 0
            if i == ")":
                popNum = prevNum.pop() + prevSign.pop() * currentNum
                prevNum[-1] += prevSign[-1] * popNum
                prevSign[-1] = 1
                currentNum = 0
        
        return prevNum[-1]