class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort(reverse = True)
        leftIndex, rightIndex = 0, len(people) - 1

        while leftIndex <= rightIndex:
            if people[leftIndex] + people[rightIndex] <= limit:
                rightIndex -= 1
            leftIndex += 1

        return leftIndex
