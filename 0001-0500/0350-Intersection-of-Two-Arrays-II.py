350. Intersection of Two Arrays IIclass Solution(object):
    def intersect(self, nums1, nums2):
        auxCounter = Counter(nums1) & Counter(nums2)
        intersection = []
        
        for v in auxCounter.keys():
            intersection += [v] * auxCounter[v]
            
        return intersection
            