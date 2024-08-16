class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)
        prevValues = defaultdict(int)
        
        def processBook(i, widthUsed, currentShelfHeight):
            if i == n:
                return currentShelfHeight
            
            if not (i, widthUsed, currentShelfHeight) in prevValues:
                bookWidth, bookHeight = books[i]
                
                if bookWidth + widthUsed <= shelfWidth:
                    if bookHeight <= currentShelfHeight:
                        returnVal = processBook(i+1, bookWidth + widthUsed, currentShelfHeight)
                    else:
                        val1 = processBook(i+1, bookWidth + widthUsed, bookHeight)
                        val2 = currentShelfHeight + processBook(i+1, bookWidth, bookHeight)
                        returnVal = min(val1, val2)
                else:
                    returnVal = currentShelfHeight + processBook(i+1, bookWidth, bookHeight)
                
                prevValues[(i, widthUsed, currentShelfHeight)] = returnVal
            
            return prevValues[(i, widthUsed, currentShelfHeight)]
        
        return processBook(0, 0, 0)