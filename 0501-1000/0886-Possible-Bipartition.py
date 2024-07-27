class Solution(object):
    def possibleBipartition(self, n, dislikes):
        # General notes about this solution:
        # > p1 and p2 represent person indices
        # > Groups are +1 or -1 if assigned, 0 if unassigned

        if n == 1 or not dislikes:
            return True

        dislikeTable = defaultdict(list)
        groupTable = defaultdict(int)

        for p1, p2 in dislikes:
            dislikeTable[p1].append(p2)
            dislikeTable[p2].append(p1)

        def canAssign(p1, group):
            if groupTable[p1] == -group:
                return False

            groupTable[p1] = group

            for p2 in dislikeTable[p1]:
                if groupTable[p2] == group:
                    return False

                if groupTable[p2] == 0 and (not canAssign(p2, -group)):
                    return False

            return True

        for p1 in range(1, n+1):
            if groupTable[p1] == 0 and (not canAssign(p1, 1)):
                return False

        return True
