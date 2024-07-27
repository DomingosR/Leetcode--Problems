def numValidNames(nameIdeas):
    # Creating an array of sets which will contain the several endings
    # of words starting with a given letter
    wordEndings = [set() for _ in range(26)]

    # Adding word endings for each possible idea to its set
    for idea in nameIdeas:
        order = ord(idea[0:1]) - ord('a')
        wordEndings[order].add(idea[1:])

    numNames = 0

    # For each pair of initials, count the number of endings in each set
    # that are not in the other, and compute number of valid names for
    # this pair or initials

    for i in range(25):
        for j in range(i+1, 26):
            k = len(wordEndings[i] & wordEndings[j])
            numNames += 2 * (len(wordEndings[i]) - k) * (len(wordEndings[j]) - k)

    return numNames

class Solution(object):
    def distinctNames(self, ideas):
        return numValidNames(ideas)