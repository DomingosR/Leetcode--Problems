class Solution(object):
    def countOfAtoms(self, formula):
        n = len(formula)
        stack = [Counter()]

        def isUpperCase(char):
            return 65 <= ord(char) <= 90

        def isLowerCase(char):
            return 97 <= ord(char) <= 122

        def isNumeric(char):
            return 48 <= ord(char) <= 57

        i = 0   
        while i < n:
            char = formula[i]

            if char == "(":
                stack.append(Counter())
                i += 1

            if char == ")":
                newCount = 0
                while i < n-1 and isNumeric(formula[i+1]):
                    i += 1
                    newCount = 10 * newCount + int(formula[i])

                newCount = max(newCount, 1)

                for element in stack[-1]:
                    stack[-1][element] *= newCount

                lastDict = stack.pop()

                for element in lastDict:
                    stack[-1][element] += lastDict[element]

                i += 1

            if isUpperCase(char):
                newElement = char
                while i < n-1 and isLowerCase(formula[i+1]):
                    i += 1
                    newElement += formula[i]

                if not (i < n-1 and isNumeric(formula[i+1])):
                    newCount = 1
                else:
                    newCount = 0
                    while i < n-1 and isNumeric(formula[i+1]):
                        i += 1
                        newCount = 10 * newCount + int(formula[i])

                stack[-1][newElement] += newCount
                i += 1

        elementInfo = [[v, stack[-1][v]] for v in stack[-1]]
        elementInfo.sort(key = lambda x: x[0])

        return "".join([ str(x[0]) + (str(x[1] if x[1] > 1 else "")) for x in elementInfo])