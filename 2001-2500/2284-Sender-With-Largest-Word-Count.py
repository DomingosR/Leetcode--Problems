class Solution(object):
    def largestWordCount(self, messages, senders):
        wordCount = Counter()
        
        def numWords(message):
            return len(message.split())
        
        for i in range(len(messages)):
            wordCount[senders[i]] += numWords(messages[i])
            
        maxCount = max(wordCount.values())
        maxSenders = [sender for sender in wordCount if wordCount[sender] == maxCount]
        maxSenders.sort()
        
        return maxSenders[-1]