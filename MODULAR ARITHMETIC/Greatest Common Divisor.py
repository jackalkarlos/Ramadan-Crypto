def gcd(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
print(gcd(66528,52920))

#or

import math
print(math.gcd(66528,52920))