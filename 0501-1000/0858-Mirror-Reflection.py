def gcd(p, q):
    while p % q:
        r = p % q
        p = q
        q = r
    return q

def lcm(p, q):
    return (p * q) // gcd(p, q)

def firstReceptor(p, q):
    n = lcm(p, q)
    t2 = n // p
    t1 = n // q
    
    if t1 % 2 == 0: return 2
    if t2 % 2 == 0: return 0
    return 1

class Solution(object):
    def mirrorReflection(self, p, q):
        return firstReceptor(p, q)