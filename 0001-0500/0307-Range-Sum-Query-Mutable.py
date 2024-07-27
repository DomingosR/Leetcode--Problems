class NumArray(object):
    def __init__(self, nums):
        self.numsArray = nums
        self.total = sum(nums)
        self.numCount = len(nums)
    
    def update(self, index, val):
        self.total -= self.numsArray[index]
        self.numsArray[index] = val
        self.total += self.numsArray[index]

    def sumRange(self, left, right):
        if right - left >= self.numCount // 2:
            return self.total - sum(self.numsArray[:left]) - sum(self.numsArray[right+1:])
        else:
            return sum(self.numsArray[left:right+1])
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)