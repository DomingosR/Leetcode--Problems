class Solution(object):
    def maxPathSum(self, root):
        def dfs(inputNode):
            currentVal = inputNode.val          # Value of current node
            maxSumEndpoint = currentVal         # Maximum sum of path in tree below with
                                                #   node as endpoint
            maxSum = currentVal                 # Maximum sum in subtree with current
                                                #   node as root
            if inputNode.left != None:
                maxSumEndpoint_L, maxSum_L = dfs(inputNode.left)
                maxSumEndpoint = max(maxSumEndpoint, currentVal + maxSumEndpoint_L)
                maxSum = max(maxSum, maxSum_L)

            if inputNode.right != None:
                maxSumEndpoint_R, maxSum_R = dfs(inputNode.right)
                maxSumEndpoint = max(maxSumEndpoint, currentVal + maxSumEndpoint_R)
                maxSum = max(maxSum, maxSum_R)

            maxSum = max(maxSum, maxSumEndpoint)
            if inputNode.left != None and inputNode.right != None:
                maxSum = max(maxSum, currentVal + maxSumEndpoint_L + maxSumEndpoint_R)

            return maxSumEndpoint, maxSum

        return dfs(root)[1]