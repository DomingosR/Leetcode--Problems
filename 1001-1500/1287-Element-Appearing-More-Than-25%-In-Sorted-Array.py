class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        k = n // 4 + 1

        n1 = arr[k-1]
        if bisect_right(arr, n1) - bisect_left(arr, n1) >= k:
            return n1

        n2 = arr[2*k-1]
        if bisect_right(arr, n2) - bisect_left(arr, n2) >= k:
            return n2

        return arr[3*k-1]
