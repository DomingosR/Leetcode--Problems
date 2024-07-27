class Solution(object):
    def discountPrices(self, sentence, discount):
        digits = set("0123456789")
        factor = 1.0 * (100 - discount) / 100
        
        def isPrice(indWord):
            if len(indWord) == 1 or indWord[0] != "$":
                return False
            
            for i in range(1, len(indWord)):
                if indWord[i] not in digits:
                    return False
            
            return True
        
        indWords = sentence.split()
        adjWords = []
        
        for i in range(len(indWords)):
            currentWord = indWords[i]
            if not isPrice(currentWord):
                adjWords.append(currentWord + " ")
            else:
                originalPrice = int(currentWord[1:])
                adjPrice = factor * originalPrice
                adjWords.append("$" + '{0:.2f}'.format(adjPrice) + " ")
        
        return "".join(adjWords)[:-1]