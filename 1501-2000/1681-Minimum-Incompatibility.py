class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        groupSize = n // k

        preComputed = defaultdict(int)
        preComputed[0] = 0

        def auxFn(bitMask): # Returns minimum incompatibility including only elements corresponding to 1 in mask
            if bitMask not in preComputed:
                optimalVal = float("inf")
                oneBits = [i for i in range(n) if (bitMask >> i) & 1]
                subCombs = combinations(oneBits, groupSize)
                for indComb in subCombs:
                    elements = [nums[i] for i in indComb]
                    if len(elements) == len(set(elements)):
                        auxBitMask = bitMask
                        for i in indComb:
                            auxBitMask ^= (1 << i)
                        optimalVal = min(optimalVal, auxFn(auxBitMask) + max(elements) - min(elements))
                
                preComputed[bitMask] = optimalVal
        
            return preComputed[bitMask]
        
        result = auxFn((1 << n) - 1)
        return -1 if result == float("inf") else result