class Solution(object):
    def isPrefixString(self, s, words):
        currStr = ""
        
        for word in words:
            currStr += word
            if currStr == s:
                return True
            if len(currStr) > len(s) or s[:len(currStr)] != currStr:
                return False
            
        return False