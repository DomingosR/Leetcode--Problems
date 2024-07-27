class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        numCounter = Counter(arr1)
        auxArray1 = []
        
        for num in arr2:
            auxArray1 += [num] * numCounter[num]
            del numCounter[num]
            
        auxArray2 = []
        for num in numCounter:
            auxArray2 += [num] * numCounter[num]
            
        return auxArray1 + sorted(auxArray2)