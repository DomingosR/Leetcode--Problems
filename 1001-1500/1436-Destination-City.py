class Solution(object):
    def destCity(self, paths):
        source, dest = list(map(list, zip(*paths)))
        diff = list(set(dest) - set(source))
        return diff[0]