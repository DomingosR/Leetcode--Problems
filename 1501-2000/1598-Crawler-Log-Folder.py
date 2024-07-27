class Solution(object):
    def minOperations(self, logs):
        count = 0
        
        for action in logs:
            if action == "../" and count:
                count -= 1
                
            if action != "../" and action != "./":
                count += 1
                             
        return count