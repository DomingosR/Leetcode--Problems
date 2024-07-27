class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        keys = ["type", "color", "name"]
        keyIndex = keys.index(ruleKey)
        return len([item for item in items if item[keyIndex] == ruleValue])
