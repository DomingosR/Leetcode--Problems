class Solution(object):
    def frequencySort(self, s):
        counterS = [(char, count) for char, count in Counter(s).items()]
        counterS.sort(key = lambda x: -x[1])
        sortedStr = ""

        for char, count in counterS:
            sortedStr += char * count

        return sortedStr
