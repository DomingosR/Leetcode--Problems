class Solution(object):
    def minAnagramLength(self, s):
        n = len(s)
        overallCounter = Counter(s)
        currentCounter = Counter()
        
        for i in range(1, n // 2 + 1):
            currentCounter[s[i-1]] += 1
            
            if n % i == 0:
                k = n // i
                if all([Counter(s[j * i: (j+1) * i]) == currentCounter for j in range(1, k)]):
                    return i
                
        return n