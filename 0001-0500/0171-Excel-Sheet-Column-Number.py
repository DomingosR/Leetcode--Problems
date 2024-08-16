class Solution(object):
    def titleToNumber(self, columnTitle):
        colNumber = 0
        
        for letter in columnTitle:
            colNumber = 26 * colNumber + (ord(letter) - ord("A") + 1)
            
        return colNumber