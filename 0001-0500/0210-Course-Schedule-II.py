class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preReqCount = [0] * numCourses
        dependentCourses = defaultdict(set)
        processed = [0] * numCourses
        courseOrder = []
        courseQueue = deque()
        
        for c2, c1 in prerequisites:
            dependentCourses[c1].add(c2)
            preReqCount[c2] += 1
            
        for c in range(numCourses):
            if preReqCount[c] == 0:
                courseQueue.appendleft(c)
                
        while courseQueue:
            c = courseQueue.pop()
            if processed[c] == 1:
                return []
            courseOrder.append(c)
            processed[c] = 1
            for c1 in dependentCourses[c]:
                preReqCount[c1] -= 1
                if preReqCount[c1] == 0:
                    courseQueue.appendleft(c1)
                    
        if len(courseOrder) == numCourses:
            return courseOrder
        return []