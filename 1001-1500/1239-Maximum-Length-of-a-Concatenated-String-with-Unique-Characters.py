class Solution(object):
    def maxLength(self, arr):
        possibleCombs = [""]
        
        for word in arr:
            if len(word) != len(set(word)):
                continue
            
            for comb in possibleCombs:
                if not (set(comb) & set(word)):
                    possibleCombs.append(word + comb)
                    
        return max([len(comb) for comb in possibleCombs])