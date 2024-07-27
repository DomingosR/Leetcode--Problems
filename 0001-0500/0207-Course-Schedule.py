class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        
        for u, v in prerequisites:
            graph[v].append(u)
            
        visitedNodes = [-1] * numCourses
        
        def explore(i):
            visitedNodes[i] = 0
            for v in graph[i]:
                if visitedNodes[v] == 0 or (visitedNodes[v] == -1 and explore(v)): 
                    return True
            visitedNodes[i] = 1
            return False
       
        for i in range(numCourses):
            if visitedNodes[i] == -1: 
                explore(i)
            if visitedNodes[i] == 0:
                return False
        
        return True   