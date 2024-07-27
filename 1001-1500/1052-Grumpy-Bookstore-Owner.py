class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        totalCustomers = sum(customers)
        grumpyAux = [customers[i] * grumpy[i] for i in range(len(customers))]
        currentGrumpy = sum(grumpyAux[:minutes])
        maxGrumpy = currentGrumpy
        
        for i in range(len(customers) - minutes):
            currentGrumpy += grumpyAux[i + minutes] - grumpyAux[i]
            maxGrumpy = max(maxGrumpy, currentGrumpy)
            
        return totalCustomers - sum(grumpyAux) + maxGrumpy