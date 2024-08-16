class Solution(object):
    def kIncreasing(self, arr, k):
        def longestNonDecSubseq(nums):
            sequence = []
            
            for num in nums:
                if not sequence or sequence[-1] <= num:
                    sequence.append(num)
                else:
                    sequence[bisect_right(sequence, num)] = num
                    
            return len(sequence)
        
        return len(arr) - sum([longestNonDecSubseq(arr[i::k]) for i in range(k)])