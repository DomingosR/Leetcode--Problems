class Solution(object):
    def searchRange(self, nums, target):
        def bisectLeft(array, k):
            if array[0] >= k:
                return 0
            if array[len(array)-1] < k:
                return len(array)

            left = 0
            right = len(array)
            while left < right:
                mid = left + (right - left) // 2
                if array[mid] < k:
                    left = mid + 1
                else:
                    right = mid

            return left

        def bisectRight(array, k):
            if array[0] > k:
                return 0
            if array[len(array)-1] <= k:
                return len(array)

            left = 0
            right = len(array)
            while left < right:
                mid = left + (right - left) // 2
                if array[mid] <= k:
                    left = mid + 1
                else:
                    right = mid

            return left

        def searchRangeForValue(inputArray, k):
            if not inputArray:
                return [-1, -1]

            bLeft = bisectLeft(inputArray, k)
            bRight = bisectRight(inputArray, k) - 1

            if inputArray[bRight] != k:
                return [-1, -1]

            return [bLeft, bRight]

        return searchRangeForValue(nums, target)
