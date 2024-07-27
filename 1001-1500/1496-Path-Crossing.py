class Solution(object):
    def isPathCrossing(self, path):
        current = 0 + 0j
        visited = set()
        visited.add(current)
        
        moves = {'N': 0 + 1j, 'S': 0 - 1j, 'E': 1 + 0j, 'W': -1 + 0j}
        
        for move in path:
            current += moves[move]
            if current in visited:
                return True
            visited.add(current)
            
        return False