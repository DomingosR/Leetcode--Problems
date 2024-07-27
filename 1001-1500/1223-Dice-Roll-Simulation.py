def totalNumSequences(n, rollMax):
    p = 1000000007
    numRolls = 0

    # This will contain the number of sequences ending in a given roll
    # repeated a certain number of times.  Thus, numSequences[i][k]
    # corresponds to the number of valid sequences ending in k rolls of i
    numSequences = []
    for j in range(6):
        numSequences.append([0] * rollMax[j])
        numSequences[j][0] = 1

    # This will contain the overall total number of sequences ending in a
    # given number, and the total number of valid sequences
    totalSequencesForEnding = [1] * 6
    totalSequences = 6

    # Main loop to compute final number
    i = 1
    while i < n:
        tempSum = 0
        for j in range(6):
            sequencesAdded = totalSequences - totalSequencesForEnding[j]
            sequencesRemoved = numSequences[j][rollMax[j]-1]

            tempSum += (sequencesAdded - sequencesRemoved)
            numSequences[j].pop(rollMax[j]-1)
            numSequences[j].insert(0, sequencesAdded)

            totalSequencesForEnding[j] += (sequencesAdded - sequencesRemoved)

        totalSequences += tempSum
        i += 1

    return (totalSequences % p)

class Solution(object):
    def dieSimulator(self, n, rollMax):
        return totalNumSequences(n, rollMax)
