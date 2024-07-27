class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        replacementInfo = []
        
        for i in range(len(indices)):
            index, source, target = indices[i], sources[i], targets[i]
            if s[index:index + len(source)] == source:
                replacementInfo.append([index, source, target])
            
        replacementInfo.sort(key = lambda x: x[0])
        n, offset = len(replacementInfo), 0
        
        for i, source, target in replacementInfo:
            j = i + offset
            s = s[:j] + target + s[j+len(source):]
            offset += len(target) - len(source)
                
        return s
        