class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key = lambda x: (-x[0], x[1]))
        queue = []
        
        for h, i in people:
            queue = queue[:i] + [[h, i]] + queue[i:]
            
        return queue