class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        attainable = []
        requirements = defaultdict(set)
        for i in range(len(recipes)):
            requirements[recipes[i]] = set(ingredients[i])
        supplyQueue = deque(supplies)
        processed = set(supplies)
        
        while supplyQueue:
            currentSupply = supplyQueue.pop()
            for recipe in requirements:
                requirements[recipe].discard(currentSupply)
                if len(requirements[recipe]) == 0 and recipe not in processed:
                    attainable.append(recipe)
                    supplyQueue.appendleft(recipe)
                    processed.add(recipe)
                                  
        return attainable