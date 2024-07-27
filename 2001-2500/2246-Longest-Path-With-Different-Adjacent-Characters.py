class Solution(object):
    def longestPath(self, parent, s):
        children = defaultdict(list)
        for i, node in enumerate(parent):
            if node >= 0:
                children[node].append(i)
        
        maxLenPath = [0]

        def dfs(node):
            lengthOfSubpaths = [0]
            for childNode in children[node]:
                cur = dfs(childNode)
                if s[node] != s[childNode]:
                    lengthOfSubpaths.append(cur)
                    
            lengthOfSubpaths = nlargest(2, lengthOfSubpaths)
            maxLenPath[0] = max(maxLenPath[0], sum(lengthOfSubpaths) + 1)
            return max(lengthOfSubpaths) + 1
        
        dfs(0)
        
        return maxLenPath[0]