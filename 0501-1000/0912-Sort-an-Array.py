class Solution(object):
    def sortArray(self, nums):
        def mergesort(inputList):
            n = len(inputList)
            if n > 1:
                midIndex = n//2
                leftList = mergesort(inputList[:midIndex])
                rightList = mergesort(inputList[midIndex:])
                inputList = merge(leftList, rightList)
            return inputList

        def merge(list1, list2):
            sortedList = []
            while list1 and list2:
                if list1[0] <= list2[0]:
                    sortedList.append(list1.pop(0))
                else:
                    sortedList.append(list2.pop(0))
            if not list1:
                sortedList.extend(list2)
            if not list2:
                sortedList.extend(list1)
            return sortedList

        return mergesort(nums)
