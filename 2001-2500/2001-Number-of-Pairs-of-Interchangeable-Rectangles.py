class Solution(object):
    def interchangeableRectangles(self, rectangles):
        def gcd(a, b):
            while a % b != 0:
                a, b = b, a % b
            return b
        
        ratios = [1.0 * rect[0]/rect[1] for rect in rectangles]
        ratioCounter = Counter(ratios)

        return sum([n * (n - 1) // 2 for n in ratioCounter.values()])