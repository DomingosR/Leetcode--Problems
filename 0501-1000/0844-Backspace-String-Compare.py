class Solution(object):
    def backspaceCompare(self, s, t):
        iS, iT = len(s)-1, len(t)-1
        numToBackS, numToBackT = 0, 0

        while True:
            while iS >= 0 and (numToBackS or s[iS] == "#"):
                numToBackS += 1 if s[iS] == "#" else -1
                iS -= 1
            while iT >= 0 and (numToBackT or t[iT] == "#"):
                numToBackT += 1 if t[iT] == "#" else -1
                iT -= 1
            if not(iS >= 0 and iT >= 0 and s[iS] == t[iT]):
                return iS == iT == -1
            iS -= 1
            iT -= 1
