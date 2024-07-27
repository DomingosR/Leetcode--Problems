class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        suggestions = []
        currentMatches = products
        
        for i in range(1, len(searchWord)+1):
            currentMatches = [word for word in currentMatches if word[:i] == searchWord[:i]]
            suggestions.append(currentMatches[:3])
            
        return suggestions