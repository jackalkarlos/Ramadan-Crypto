import random
import math
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from sympy import mod_inverse

def encrypt(plaintext):
        p = getPrime(2048)
        q = getPrime(2048)
        n = p * q
        tot = (p-1) * (q-1)
        e = random.randrange(2, tot)
        while math.gcd(e, tot) != 1:
                e = random.randrange(2, tot)
        d = mod_inverse(e, tot)
        intstr = bytes_to_long(plaintext.encode())
        encrypted = pow(intstr,e,n)
        return encrypted, d, n

def decrypt(cipherint, d, n):
        m = pow(cipherint, d, n)
        return long_to_bytes(m).decode()
