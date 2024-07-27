class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        differences = [arr[i] - arr[i-1] for i in range(1, len(arr))]
        return min(differences) == max(differences)