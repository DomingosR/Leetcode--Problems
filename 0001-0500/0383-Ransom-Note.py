class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazineCounter = Counter(magazine)
        ransomCounter = Counter(ransomNote)
        magazineCounter.subtract(ransomCounter)
        return min(magazineCounter.values()) >= 0