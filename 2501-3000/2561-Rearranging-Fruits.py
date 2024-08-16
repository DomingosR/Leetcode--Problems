class Solution(object):
    def minCost(self, basket1, basket2):
        counter1, counter2 = Counter(basket1), Counter(basket2)
        overall = counter1 + counter2

        if any([overall[v] % 2 for v in overall]):
            return -1
        
        list1, list2 = [], []
        allValues = sorted([v for v in overall])
        minVal = allValues[0]
        
        for v in allValues:
            if counter1[v] > counter2[v]:
                list1 += [v] * ((counter1[v] - counter2[v]) // 2)
            elif counter2[v] > counter1[v]:
                list2 += [v] * ((counter2[v] - counter1[v]) // 2)
        
        n = len(list1)
        return sum([min(list1[i], list2[n-1-i], 2*minVal) for i in range(n)])
            