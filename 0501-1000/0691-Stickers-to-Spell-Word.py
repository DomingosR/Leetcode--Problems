class Solution(object):
    def minStickers(self, stickers, target):
        allStickers = "".join(stickers)
        if len(set(target) - set(allStickers)) > 0:
            return -1
        
        n = len(target)
        stickerCounters = [Counter(sticker) for sticker in stickers]
        seenStrings = defaultdict(int)
        
        def minStickers(indStr):
            if not indStr:
                return 0
            
            if indStr in seenStrings:
                return seenStrings[indStr]
            
            numStickers = n
            indStrCounter = Counter(indStr)
            
            for indCounter in stickerCounters:
                if indStr[0] in indCounter:
                    auxStr = "".join(char * k for char, k in (indStrCounter - indCounter).items())
                    numStickers = min(numStickers, 1 + minStickers(auxStr))
            
            seenStrings[indStr] = numStickers
            return numStickers
            
        return minStickers(target)