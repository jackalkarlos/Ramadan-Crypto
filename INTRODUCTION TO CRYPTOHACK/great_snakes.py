#!/usr/bin/env python3

import sys

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

#TR: ASCII kodlarını içeren bir liste veriliyor. "ords" listesi.
#TR: Öncelikle for o in ords döngüsü ords listesindeki her bir elemanı alır ve o değişkenine atar.
#TR: Daha sonra, bu eleman 0x32 sayısı ile XOR işlemine tabi tutulur. 
#TR: Sonuçta, elde edilen sayısal değer, chr() fonksiyonu kullanılarak karaktere dönüştürülür. 
#TR: Bu işlemler tüm listedeki elemanlar için tekrarlanır.
#TR: En son adımda ise, tüm karakterler join() metodu kullanılarak birleştirilir ve ekrana yazdırılır.

#EN: There is a ASCII numbers list with the name "ords".
#EN: Firstly, the "for o in ords" loop takes each element in the "ords" list and assigns it to the variable "o".
#EN: Next, this variables is XORed with the number 0x32.
#EN: The resulting numeric value is converted to a character using the chr() function.
#EN: These operations are repeating for the elements in the variable list.

print("Here is your flag:")

print("".join(chr(o ^ 0x32) for o in ords))
