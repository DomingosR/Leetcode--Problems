class Solution(object):
    def minimumTime(self, n, relations, time):
        nextCourses = defaultdict(list)
        numPreReq = [0] * n
        
        for prevCourse, nextCourse in relations:
            prevCourse -= 1
            nextCourse -= 1
            nextCourses[prevCourse].append(nextCourse)
            numPreReq[nextCourse] += 1
        
        courseQueue = deque()
        courseTime = [0] * n

        for i in range(n):
            if numPreReq[i] == 0:
                courseQueue.appendleft(i)

        while courseQueue:
            currCourse = courseQueue.pop()
            courseTime[currCourse] += time[currCourse]
            
            for nextCourse in nextCourses[currCourse]:
                courseTime[nextCourse] = max(courseTime[nextCourse], courseTime[currCourse])
                numPreReq[nextCourse] -= 1
                if numPreReq[nextCourse] == 0:
                    courseQueue.appendleft(nextCourse)

        return max(courseTime)