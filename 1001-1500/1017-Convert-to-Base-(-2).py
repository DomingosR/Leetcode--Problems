class Solution(object):
    def baseNeg2(self, n):
        if n == 0:
            return "0"
        
        representation = []
        while n > 0:
            representation.append(n % 2)
            n >>= 1
            
        i = 0
        while i < len(representation):
            if representation[i] == 0:
                i += 1
            else:
                if i == len(representation) - 1:
                    representation.append(0)
                while representation[i] >= 2:
                    representation[i] -= 2
                    representation[i+1] += 1
                if representation[i] == 1 and (i % 2):
                    representation[i+1] += 1
                i += 1
        
        while representation[-1] == 0:
            representation.pop()
            
        representation = representation[::-1]
        return "".join([str(num) for num in representation])