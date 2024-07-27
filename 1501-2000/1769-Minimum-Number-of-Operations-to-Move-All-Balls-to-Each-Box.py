class Solution(object):
    def minOperations(self, boxes):
        answer, left, right = [0], 0, -int(boxes[0])
        
        for i in range(len(boxes)):
            right += int(boxes[i])
            answer[0] += i * int(boxes[i])
            
        for i in range(1, len(boxes)):
            left += int(boxes[i-1])
            answer.append(answer[-1] + left - right)
            right -= int(boxes[i])
            
        return answer