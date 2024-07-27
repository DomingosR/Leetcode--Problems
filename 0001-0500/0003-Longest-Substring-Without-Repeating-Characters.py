class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        seenCharacters = {}

        leftPointer = 0
        subStrLen = 0

        for rightPointer in range(n):
            if s[rightPointer] not in seenCharacters:
                subStrLen = max(subStrLen, rightPointer - leftPointer + 1)
            else:
                if seenCharacters[s[rightPointer]] < leftPointer:
                    subStrLen = max(subStrLen, rightPointer - leftPointer + 1)
                else:
                    leftPointer = seenCharacters[s[rightPointer]] + 1
            seenCharacters[s[rightPointer]] = rightPointer

        return subStrLen
