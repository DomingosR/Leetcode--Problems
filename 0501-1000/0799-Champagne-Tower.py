class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        nextQuantities = [poured]
        
        for currRow in range(query_row):        
            currQuantities = nextQuantities
            nextQuantities = [0] * (currRow + 2)

            for i in range(currRow + 2):
                if i < currRow + 1:
                    nextQuantities[i] += 1.0 * max(currQuantities[i] - 1, 0) / 2
                if i > 0:
                    nextQuantities[i] += 1.0 * max(currQuantities[i-1] - 1, 0) / 2
            
        return min(nextQuantities[query_glass], 1)