class Solution(object):
    def validateStackSequences(self, pushed, popped):
        n = len(pushed)
        newPushed = []
        i = 0
        j = 0

        while i < n:
            if pushed[i] == popped[j]:
                j += 1
                while j < n and newPushed and popped[j] == newPushed[-1]:
                    newPushed.pop()
                    j += 1
            else:
                newPushed.append(pushed[i])

            i += 1

        while j < n and popped[j] == newPushed[-1]:
            newPushed.pop()
            j += 1

        return not newPushed
