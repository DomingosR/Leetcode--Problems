class Solution(object):
    def minimumDeletions(self, s):
        minNetCount, netCountB, n = 0, 0, len(s)
        
        for i in range(len(s)):
            netCountB += (1 if s[i] == "b" else -1)
            minNetCount = min(minNetCount, netCountB)
            
        return (n - netCountB) // 2 + minNetCount