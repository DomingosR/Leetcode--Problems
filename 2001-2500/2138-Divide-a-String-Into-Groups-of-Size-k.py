class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        splits = []
        i = 0
        
        while i < len(s):
            splits.append(s[i: min(k + i, len(s))] + fill * max(k - (len(s) - i), 0))
            i += k
            
        return splits