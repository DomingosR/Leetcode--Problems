class Solution(object):
    def equalFrequency(self, word):
        # This problem has a number of special cases that need to be dealt with
        letterCounter = Counter(word)
        
        # If there is only one letter in the string, return True
        if len(letterCounter) == 1: return True
        
        # If the frequency of every letter is 1, return True
        if max(letterCounter.values()) == 1: return True
        
        freqCounter = Counter(letterCounter.values())
        minFreq, maxFreq = min(freqCounter.keys()), max(freqCounter.keys())
        
        # If there are not exactly two frequencies, return False
        # (Note that if there is only one frequency it must not be 1, that case has been covered)
        if len(freqCounter) != 2: return False
        
        # If there is a single sole letter and all others have the same frequency, return True
        if minFreq == 1 and freqCounter[minFreq] == 1: return True
        
        # If the maximum frequency exceeds the minimum by 1, and there is only one element
        # with that frequency, return True
        if freqCounter[maxFreq] == 1 and maxFreq == minFreq + 1: return True
        
        # For all other cases, return False
        return False