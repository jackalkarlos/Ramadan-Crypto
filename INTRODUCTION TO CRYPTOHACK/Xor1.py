from pwn import xor
#TR: Keyler önce hex'ten byte'a dönüştürülüyor.
#Xor yaparken sıranın bir farkı olmadığını öğrenmiştik.
#Key2 için tek yapmamız gereken key1 ile "key1 ^ key2" değerini xorlamak olacaktır.
#Key3 içinde aynı işlemi yapacağız. Key3 için key2 ile "key2 ^ key3" değerine xor işlemi uyguluyoruz.
#Son olarak hepsine aynı anda xor işlemi uyguluyoruz ve sonucu elde ediyoruz.
#Aslında yaptığımız amelelik sayılabilir, çünkü tüm değerleri aynı anda xorlasak yine sonucu elde ediyoruz.

#EN: Keys are converted from hex to bytes first.
#We learned that there is no difference in order when doing xor.
#For key2, all we have to do is xor the key1 with the value "key1 ^ key2".
#We will do the same for key3. For Key3, we xor the value of "key2 ^ key3" with key2.
#Finally, we apply xor to all of them at the same time and we get the result.
#Actually, what we do can be considered hard work, because if we evaluate all the values at the same time, we still get the result.
###
#from pwn import xor
#k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
#k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
#flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
#print(xor(k1,k2_3,flag))
###
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key3_1 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_KEY1_KEY3_KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2=xor(key2_1,key1)
key3=xor(key3_1,key2)

allkey=xor(key1,key2,key3)
flag=xor(allkey,FLAG_KEY1_KEY3_KEY2)
print(flag.decode('utf-8'))
