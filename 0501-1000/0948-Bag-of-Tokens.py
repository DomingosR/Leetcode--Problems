class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        score = 0
        currentVal = 0

        tokenQueue = deque(sorted(tokens))

        while tokenQueue and (tokenQueue[0] <= power or currentVal):
            if tokenQueue[0] <= power:
                power -= tokenQueue.popleft()
                currentVal += 1
            else:
                power += tokenQueue.pop()
                currentVal -= 1
            score = max(score, currentVal)

        return score
