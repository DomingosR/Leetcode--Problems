class Solution(object):
    def simplifyPath(self, path):
        elementStack = []
        tokens = path.split("/")

        for token in tokens:
            if token == "..":
                if elementStack:
                    elementStack.pop()
            elif token and token != ".":
                elementStack.append(token)

        return '/' + '/'.join(elementStack)
