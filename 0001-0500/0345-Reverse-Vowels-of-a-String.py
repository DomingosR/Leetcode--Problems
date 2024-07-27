class Solution(object):
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        sList = list(s)
        leftPointer = 0
        rightPointer = len(s) - 1
        
        while leftPointer < rightPointer:
            while leftPointer < n and sList[leftPointer] not in vowels:
                leftPointer += 1
            while rightPointer >= 0 and sList[rightPointer] not in vowels:
                rightPointer -= 1
            if 0 <= leftPointer < rightPointer < n:
                temp = sList[leftPointer]
                sList[leftPointer] = sList[rightPointer]
                sList[rightPointer] = temp
                leftPointer += 1
                rightPointer -= 1
        
        return ''.join(sList)