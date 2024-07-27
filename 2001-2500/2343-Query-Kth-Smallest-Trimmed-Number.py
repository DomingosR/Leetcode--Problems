class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        returnVal = []
        trimmedNumbers = {}

        for [k, trim] in queries:
            trimmedNumbers.setdefault(trim, \
                    sorted([(num[-trim:], i) for i, num in enumerate(nums)]))
            returnVal.append(trimmedNumbers[trim][k-1][1])

        return returnVal