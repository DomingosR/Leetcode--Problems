class Solution(object):
    def possiblyEquals(self, s1, s2):
        def possibleVals(s):
            values = {int(s)}
            for i in range(1, len(s)):
                values |= {n1 + n2 for n1 in possibleVals(s[:i])  \
                                   for n2 in possibleVals(s[i:])}
            return values

                
        previousValues = defaultdict(int)
        n1, n2 = len(s1), len(s2)
        
        # Returns True if s1[i:] and s2[j:] are compatible, given that we expect
        # that s1[i:] will have diff more characters than s2[j:]
        # Examples: s1[i:] = "1abc", s2[j:] = "abc", diff = 1 returns True
        #           s1[i:] = "abc", s2[j:] = "bc", diff = 1 returns True
        #           s1[i:] = "1bc", s2[j:] = "abc", diff = 0 returns True
        
        def process(i, j, diff):
            if (i, j, diff) in previousValues:
                return previousValues[(i, j, diff)]
            
            if i == n1 and j == n2:
                previousValues[(i, j, diff)] = (diff == 0)
                return previousValues[(i, j, diff)]

            if (i < n1 and s1[i].isdigit()) or (j < n2 and s2[j].isdigit()):
                values1, values2 = {0}, {0}
                i1, j1 = i, j

                while i1 < n1 and s1[i1].isdigit():
                    i1 += 1
                if i1 > i:
                    values1 = possibleVals(s1[i:i1])

                while j1 < n2 and s2[j1].isdigit():
                    j1 += 1
                if j1 > j:
                    values2 = possibleVals(s2[j:j1])
                
                adjDiff = {n1 - n2 for n1 in values1 for n2 in values2}
                for n in adjDiff:
                    if process(i1, j1, diff - n):
                        previousValues[(i, j, diff)] = True
                        return previousValues[(i, j, diff)]
                
                previousValues[(i, j, diff)] = False
                return previousValues[(i, j, diff)]
            else:
                if i == n1:
                    if diff >= 0:
                        previousValues[(i, j, diff)] = False
                        return previousValues[(i, j, diff)]
                    return process(i, j + 1, diff + 1)
                elif j == n2:
                    if diff <= 0:
                        previousValues[(i, j, diff)] = False
                        return previousValues[(i, j, diff)]
                    return process(i + 1, j, diff - 1)
                else:
                    if diff == 0:
                        if s1[i] == s2[j]:
                            return process(i + 1, j + 1, diff)
                        else:
                            previousValues[(i, j, diff)] = False
                            return previousValues[(i, j, diff)]
                    
                    elif diff > 0:
                        return process(i + 1, j, diff - 1)
                    
                    else:
                        return process(i, j + 1, diff + 1)
                    
        return process(0, 0, 0)  