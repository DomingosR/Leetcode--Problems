class Solution(object):
    def commonChars(self, words):
        counters = [Counter(word) for word in words]
        currentCounter = counters[0]
        
        for i in range(1, len(counters)):
            currentCounter &= counters[i]
            
        outputList = []
        
        for letter in currentCounter:
            for _ in range(currentCounter[letter]):
                outputList.append(letter)
                
        return outputList