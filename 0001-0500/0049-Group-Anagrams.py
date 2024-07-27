class Solution(object):
    def groupAnagrams(self, strs):
        groupedWords = []
        groups = defaultdict(list)

        for word in strs:
            orderedWord = tuple(sorted(word))
            groups[orderedWord].append(word)

        return list(groups.values())
