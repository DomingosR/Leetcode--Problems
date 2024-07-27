class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        indices = list(range(n))
        allInfo = list(map(list, zip(positions, directions, healths, indices)))
        allInfo.sort(key = lambda x: x[0])
        
        answer = []
        stack = []
        
        for info in allInfo:
            if info[1] == "L":
                while stack and stack[-1][2] < info[2]:
                    stack.pop()
                    info[2] -= 1
                if not stack:
                    answer.append(info)
                else:
                    if stack[-1][2] == info[2]:
                        stack.pop()
                    else:
                        stack[-1][2] -= 1
            else:
                stack.append(info)
                        
        answer += stack
        
        if not answer:
            return []
        
        answer.sort(key = lambda x: x[3])
        return [answer[i][2] for i in range(len(answer))]