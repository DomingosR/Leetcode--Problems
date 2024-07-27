class Solution(object):
    def evalRPN(self, tokens):
        operations = {"+", "-", "*", "/"}
        operands = []
        n = len(tokens)
        
        for i in range(n):
            if tokens[i] in operations:
                operation = tokens[i]
                val2 = operands.pop()
                val1 = operands.pop()
                
                if operation == "+": result = val1 + val2
                if operation == "-": result = val1 - val2
                if operation == "*": result = val1 * val2
                if operation == "/": result = int(1.0 * val1 / val2)

                operands.append(result)
            
            else:
                operands.append(int(tokens[i]))
        
        return operands[0]