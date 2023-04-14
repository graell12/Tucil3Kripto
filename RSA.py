import random

primeUnder1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
   67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
   157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
   251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349, 
   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 
   457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
   571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 
   673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
   797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 
   911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def miller_rabin_test(x: int) -> bool:
    r = 0
    s = x-1
    while s % 2 == 0:
        s >>= 1
        r += 1
    if not (2 ** r * s == x - 1):
        return False

    def trial(test):
        if pow(test, s, x) == 1:
            return False
        for i in range(r):
            if pow(test, 2 ** i * s, x) == x - 1:
                return False
        else:
            return True

    for i in range(5):
        test = random.randrange(2, x)
        if trial(test):
            return False
    return True


def primeNumber(x):
    if (x < 2):
        return False
    
    if x in primeUnder1000:
        return True
    for i in primeUnder1000:
        if (x % i == 0):
            return False
    
    return miller_rabin_test(x)

def randomPrimeCandidate(keysize = 512):
    while True:
        x = random.randrange(pow(2, keysize - 1), pow(2, keysize))
        if (primeNumber(x)):
            return x

def keyGenerator(keysize = 512):
    e = 0
    d = 0
    N = 0

    p = randomPrimeCandidate(keysize)
    q = randomPrimeCandidate(keysize)

    N = p * q
    phi = (p - 1)*(q - 1)

    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (relatifPrima(e,phi)):
            break

    d = int(kunciPrivatD(phi, e))

    return e, d, N

def relatifPrima(x, y):
   while(y):
       x, y = y, x % y
   if x == 1:
       return True
   else:
       return False

def kunciPrivatD(phi, e):
    return pow(e, -1, phi)

def enkripsiRSA(text, e, n):
    return pow(text, e, n)

def dekripsiRSA(cipher, d, n):
    return pow(cipher, d, n)