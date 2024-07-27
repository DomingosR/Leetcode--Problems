class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        cumSums = list(accumulate(sorted(nums)))
        return [bisect_right(cumSums, query) for query in queries]
