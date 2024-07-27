class Solution(object):
    def minMutation(self, startGene, endGene, geneBank):
        geneQueue = deque([(startGene, 0)])
        seenGenes = {startGene}

        while geneQueue:
            currentGene, numSteps = geneQueue.pop()
            if currentGene == endGene:
                return numSteps

            for i in range(len(currentGene)):
                for indGene in "ACGT":
                    nextGene = currentGene[:i] + indGene + currentGene[i + 1:]
                    if (nextGene in geneBank) and (nextGene not in seenGenes) :
                        geneQueue.appendleft((nextGene, numSteps + 1))
                        seenGenes.add(nextGene)

        return -1 
