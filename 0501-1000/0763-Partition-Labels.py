class Solution(object):
    def partitionLabels(self, s):
        letterIndices = defaultdict(list)
        
        for i, letter in enumerate(s):
            if letter not in letterIndices:
                letterIndices[letter] = [i, i]
            else:
                letterIndices[letter][1] = i
                
        intervals = []
        
        for start, end in letterIndices.values():
            left = bisect_left(intervals, start)
            right = bisect_right(intervals, end)
            toInclude = []
            if left % 2 == 0:
                toInclude.append(start)
            if right % 2 == 0:
                toInclude.append(end)
            intervals[left:right] = toInclude
        
        n = len(intervals) // 2
        
        return [intervals[2*i+1] - intervals[2*i] + 1 for i in range(n)]