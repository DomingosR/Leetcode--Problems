class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        def freqSmallest(word):
            baseline, minOrd, count = ord('a'), 26, 0
            for char in word:
                currentOrd = ord(char) - baseline
                if currentOrd < minOrd:
                    minOrd = currentOrd
                    count = 1
                elif currentOrd == minOrd:
                    count += 1
            return count
        
        n = len(words)
        freqList = [freqSmallest(word) for word in words]
        freqList.sort()
        answer = []
        
        for queryWord in queries:
            answer.append(n - bisect_right(freqList, freqSmallest(queryWord)))
            
        return answer