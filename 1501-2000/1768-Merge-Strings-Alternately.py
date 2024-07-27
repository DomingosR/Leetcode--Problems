class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(char1 + char2 for char1, char2 \
               in zip_longest(word1, word2, fillvalue=''))