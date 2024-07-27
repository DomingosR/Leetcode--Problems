class Solution(object):
    def getCoprimes(self, nums, edges):
        def gcd(num1, num2):
            while num2:
                num1, num2 = num2, num1 % num2
            return num1

        # Pre-compute list of coprime numbers
        n = len(nums)
        coprimes = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, i+1):
                if gcd(i, j) == 1:
                    coprimes[i].append(j)
                    coprimes[j].append(i)

        # Compute list of connected nodes
        connectedNodes = defaultdict(list)
        for node1, node2 in edges:
            connectedNodes[node1].append(node2)
            connectedNodes[node2].append(node1)

        returnVal = [-1] * n                # Node number of the closest coprime ancestor 
        nodeLevels = [0] * n                # Distance from root node
        nodeQueue = deque()                 # Queue with (node number, ancestor values and \
                                            #    respective node numbers, level)

        # Start iteration with root node
        nodeQueue.appendleft([0, {}, 0])

        while nodeQueue:
            # Pop node from list of nodes
            nodeNum, ancestors, nodeLevel = nodeQueue.pop()
            nodeVal = nums[nodeNum]

            # If node has ancestors, find those with values that are coprime to its value
            if ancestors:
                coprimeNodes = [ancestors[i] for i in ancestors.keys() if i in coprimes[nodeVal]]
                # If there are such ancestor nodes, find one with the highest level
                if coprimeNodes:
                    returnVal[nodeNum] = max(coprimeNodes, key = lambda x: nodeLevels[x])
            
            # Add connected nodes to queue
            if connectedNodes[nodeNum]:
                # First, copy ancestors, and add current node to it
                tempDict = ancestors.copy()
                tempDict[nums[nodeNum]] = nodeNum
                for nextNode in connectedNodes[nodeNum]:
                    nodeLevels[nextNode] = nodeLevel + 1
                    nodeQueue.appendleft([nextNode, tempDict, nodeLevel + 1])
                    connectedNodes[nextNode].remove(nodeNum)
            
            connectedNodes[nodeNum] = []
        
        return returnVal