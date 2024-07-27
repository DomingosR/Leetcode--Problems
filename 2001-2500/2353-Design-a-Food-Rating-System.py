class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        self.foodList = defaultdict()
        self.cuisineFoods = defaultdict(list)
        
        for i in range(len(foods)):
            self.foodList[foods[i]] = [ratings[i], cuisines[i]]
            heappush(self.cuisineFoods[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food, newRating):
        self.foodList[food][0] = newRating
        cuisine = self.foodList[food][1]
        heappush(self.cuisineFoods[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        while True:
            rating, food = self.cuisineFoods[cuisine][0]
            if self.foodList[food][0] == -rating:
                return food
            else:
                heappop(self.cuisineFoods[cuisine])