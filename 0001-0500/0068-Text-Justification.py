class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justifiedLine(start, end):
            wordCount = end - start + 1
            
            if wordCount == 1 or end == len(words) - 1:
                auxStr = " ".join(words[start : end + 1])
                return auxStr + " " * (maxWidth - len(auxStr))
            
            totalNumSpaces = maxWidth - sum([len(words[i]) for i in range(start, end + 1)])
            
            basicNumSpaces = totalNumSpaces // (wordCount - 1)
            extraSpaces = totalNumSpaces % (wordCount - 1)
            
            finalLine = ""
            
            for i in range(end - start + 1):
                finalLine += words[start + i]
                if i < end - start:
                    finalLine += " " * (basicNumSpaces + 1 if i < extraSpaces else basicNumSpaces)
                    
            return finalLine
        
        justifiedText = []
        
        start = 0
        while start < len(words):
            end = start
            totalNumChars = len(words[end])
            while end + 1 < len(words) and totalNumChars + len(words[end + 1]) + 1 <= maxWidth:
                end += 1
                totalNumChars += len(words[end]) + 1
            justifiedText.append(justifiedLine(start, end))
            start = end + 1
            
        return justifiedText