class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        markedIndices = set()
        totalSum = sum(nums)
        answer = []
        
        numHeap = []
        for i, num in enumerate(nums):
            heapq.heappush(numHeap, (num, i))
            
        for i, count in queries:
            if i not in markedIndices:
                markedIndices.add(i)
                totalSum -= nums[i]
            
            while numHeap and count > 0:
                num, j = heapq.heappop(numHeap)
                if j not in markedIndices:
                    markedIndices.add(j)
                    totalSum -= num
                    count -= 1
                    
            answer.append(totalSum)
            
        return answer
        