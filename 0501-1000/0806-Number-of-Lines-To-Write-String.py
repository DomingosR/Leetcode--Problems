class Solution(object):
    def numberOfLines(self, widths, s):
        lines, currWidth = 1, 0

        for c in s:
            width = widths[ord(c) - ord('a')]
            if width + currWidth > 100:
                lines += 1
                currWidth = width
            else:
                currWidth += width

        return [lines, currWidth]
