def oklid(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        if a > b:
            a, b = b, a % b
        else:
            b, a = a, b % a
    return a


sonuc = oklid(270, 192)
print("Oklid: ", sonuc)
