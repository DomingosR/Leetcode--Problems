class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        numStack = []
        nextGreaterDict = defaultdict()

        for n in nums2:
            while numStack and numStack[-1] < n:
                nextGreaterDict[numStack.pop()] = n
            numStack.append(n)

        return [nextGreaterDict.get(x, -1) for x in nums1]