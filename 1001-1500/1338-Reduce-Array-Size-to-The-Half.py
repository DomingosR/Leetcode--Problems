from collections import Counter

def reduceToHalf(inputArray):
    target = (len(inputArray) + 1) // 2
    frequency = Counter(inputArray).most_common()

    count, i = 0, 0
    while count < target:
        count += frequency[i][1]
        i += 1
    
    return i

class Solution(object):
    def minSetSize(self, arr):
        return reduceToHalf(arr)