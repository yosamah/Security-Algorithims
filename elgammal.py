def gcdExtended(q: int, num: int)-> int:
 
    # Base Case if divisor = 0
    if q == 0:
        return num, 0, 1
 
    # Recursion but on diff inputs 
    gcd, xGcd, yGcd = gcdExtended(num % q, q)
 
    x = yGcd - (num//q) * xGcd
    y = xGcd
 
    return gcd, x, y
 
def getPositiveModuloInverse(divisor: int, num: int)->int:
    _, _, inverseModulo = gcdExtended(divisor, num)
    while inverseModulo < 0:
        inverseModulo += divisor
    return inverseModulo
 

def elGamalDecryption(xa: int, q: int, c1: int, c2: int)-> int:
    K: int = (c1 ** xa) % q
    return ((c2%q)* getPositiveModuloInverse(q, K)) % q

print(elGamalDecryption(5, 19, 11, 5))
print(getPositiveModuloInverse(1759,550))
