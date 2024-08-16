class Solution(object):
    def mergeStones(self, stones, k):
        # First, note that in each move the number of piles in the
        # array is reduced by (k-1).  If we're going to end up with 
        # only one pile, it has to be the case that n % (k-1) == 1,
        # where n = len(stones)
        n = len(stones)
        if (n-1) % (k-1):
            return -1
        
        # Compute prefix sum for later use
        prefixSum = [0] * (n+1)
        for i, num in enumerate(stones):
            prefixSum[i+1] = prefixSum[i] + num
            
        # Store previous values of dp function
        prevValues = defaultdict(int)
        
        # Main computation
        def minCostInterval(i, j):
            if j-i+1 < k:
                return 0
            
            if (i, j) not in prevValues:
                # In order to see that we can skip m below by (k-1), 
                # a simple graphical analysis will suffice
                minCost = min([minCostInterval(i, m) \
                               + minCostInterval(m+1, j) \
                               for m in range(i, j, k-1)])
                if (j-i) % (k-1) == 0:
                    minCost += (prefixSum[j+1] - prefixSum[i])
                
                prevValues[(i, j)] = minCost
                
            return prevValues[(i, j)]
        
        # Compute cost for entire interval
        return minCostInterval(0, n-1)