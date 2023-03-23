#!/usr/bin/env python3

import sys

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

#TR: ASCII kodlarını içeren bir liste veriliyor. "ords" listesi.
#EN: There is a ASCII numbers list with the name "ords".

print("Here is your flag:")
#TR: İlk başta liste arada boşluk olmaksızın birleştiriliyor. Örneğin: 81647566...
#Ardından ASCII kodlarından normal karakterlere bir dönüşüm yapılıyor.
#Ardından "0x32" hex kodu ile XOR yapılıyor.
#Son olarak sonuç yazdırılıyor.

#EN: Firstly the list is combined with no spaces. For example: 81647566...
#Then a conversion is done from ASCII codes to characters.
#Then XOR is done with "0x32" hex code.
#Finally the result is printed.
print("".join(chr(o ^ 0x32) for o in ords))
