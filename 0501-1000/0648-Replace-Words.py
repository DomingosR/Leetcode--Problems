class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key = lambda x: (len(x), x))
        words = sentence.split()   
        
        for i, word in enumerate(words):
            for key in dictionary:
                if word[:len(key)] == key:
                    words[i] = key
                    break
                        
        return " ".join(words)  