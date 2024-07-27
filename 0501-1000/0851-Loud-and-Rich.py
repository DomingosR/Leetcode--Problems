class Solution(object):
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        quietest = [-1] * n
        richerPeople = defaultdict(list)
        
        for u, v in richer:
            richerPeople[v].append(u)
            
        def processPerson(u):
            if quietest[u] < 0:
                quietest[u] = u
                for v in richerPeople[u]:
                    quietV = processPerson(v)
                    if quiet[quietV] < quiet[quietest[u]]:
                        quietest[u] = quietV
                    
            return quietest[u]
        
        for u in range(n):
            processPerson(u)
            
        return quietest