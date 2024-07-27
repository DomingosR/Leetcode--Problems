class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        processed = defaultdict(set)
        processed[len(s)].add("")
        
        def processSubStr(start):
            if start in processed:
                return processed[start]
            
            returnVal = set()
            for word in wordDict:
                if s[start:start + len(word)] == word:
                    for nextStr in processSubStr(start + len(word)):
                        returnVal.add(word + (" " + nextStr if nextStr else ""))
            
            processed[start] = returnVal
            return returnVal
        
        return processSubStr(0)