class TreeAncestor(object):

    def __init__(self, n, parent):
        self.m = 16
        
        # The i-th row of the below will contain the 2**i-th ancestor of each node
        self.ancestors = [parent] + [[-1] * n for _ in range(self.m-1)]
        for i in range(1, self.m):
            for j in range(n):
                if self.ancestors[i-1][j] != -1:
                    self.ancestors[i][j] = self.ancestors[i-1][self.ancestors[i-1][j]]
                
    def getKthAncestor(self, node, k):
        while k > 0 and node != -1:
            i = int(log(k, 2))
            node = self.ancestors[i][node]
            k -= (1 << i)
        return node      