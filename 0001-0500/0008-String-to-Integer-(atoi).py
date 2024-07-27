class Solution(object):
    def myAtoi(self, s):
        start = 0
        while start < len(s) and s[start] == " ":
            start += 1
        if start >= len(s):
            return 0

        digits = set("0123456789")

        sign = +1
        if s[start] == "+":
            start += 1
        elif s[start] == "-":
            sign = -1
            start += 1

        end = start
        while end < len(s) and s[end] in digits:
            end += 1

        auxStr = s[start:end]
        if auxStr == "":
            return 0
        auxInt = int(auxStr)

        if sign == +1:
            return min(auxInt, 2**31 - 1)
        else:
            return - min(auxInt, 2**31)
