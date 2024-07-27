class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        
        i, j = len(players) - 1, len(trainers) - 1
        matches = 0
        
        while i >= 0 and j >= 0:
            while i >= 0 and players[i] > trainers[j]:
                i -= 1
            if i >= 0:
                matches += 1
                i -= 1
            j -= 1
            
        return matches