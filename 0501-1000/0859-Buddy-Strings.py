class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal) or len(s) == 1:
            return False

        if s == goal:
            letterCounter = Counter(s)
            return True if max(letterCounter.values()) >= 2 else False

        diffIndices = [i for i in range(len(s)) if s[i] != goal[i]]

        if len(diffIndices) != 2:
            return False

        i, j = diffIndices[0], diffIndices[1]

        return True if s[i] == goal[j] and s[j] == goal[i] else False
