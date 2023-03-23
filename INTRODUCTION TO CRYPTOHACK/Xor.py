#Short Solution
from pwn import *
a = xor("label",13)
print(a.decode('utf-8'))

#Solution 2
s="label"
x= list(map(str,s))
list2=[]

for i in x:
    list2.append(chr(ord(i)^ 13))
result = "".join(list2)

print(result)

#0110 ^ 1010 = 1100

#A	B	Çıktı
#0	0	0
#0	1	1
#1	0	1
#1	1	0

#Teorikte sayı önce ondalıktan ikiliye çevirilir, sonrasında XOR yapılır.