class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        itemWeights = defaultdict(int)

        for value, weight in items1:
            itemWeights[value] += weight
        for value, weight in items2:
            itemWeights[value] += weight

        weightList = [[i, itemWeights[i]] for i in itemWeights.keys()]
        weightList.sort(key = lambda x: x[0])

        return weightList
