class Solution(object):
    def restoreString(self, s, indices):
        return ''.join([char for (_, char) in sorted(zip(indices, s))])