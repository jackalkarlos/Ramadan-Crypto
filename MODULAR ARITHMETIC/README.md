<h2>Bir sayının modunu almak için:</h2>
Bölümün kalanından kalan sayı alınır.<br>
Örneğin:<br>
10'un 5e modu 0'dır. 
11'in 5e modu 1'dir.

<h2>Küçük bir sayının büyüğe modu:</h2>

Örneğin, 3 sayısının 11e modunu almak için:<br>
Aritmetik diziler birbirini takip ederler. Yani dizi şu şekilde takip eder: "1,2,3,4,5,6,7,8,9,10,0"
Buna göre 3 sayısına 11 eklediğimizde alacağımız mod sonucu değişmez.
11 + 3 = 14
14'ün 11e modunu alırız.
Cevap 3'tür.

<h2>Negatif bir sayının modunu almak:</h2>

Küçük bir sayının büyüğüne modunu alırken yaptığımız tekniğin aynısı kullanılır.
Üstüne mod katsayısı kadar sayı eklenir.
Örneğin:<br>
-3 mod 11 için:<br>
-3 + 11 = 8'dir.<br>
8'in 11e modunu alamayız, bir kez daha 11 eklenir.<br>
19'un 11'e modunu alırız. Cevap <b>8</b> olur.<br>


<h2>Denklik bağıntısı:</h2>

Örneğin:<br>
x ≡ 17 (mod 5) için:
Önce 17'nin 5e modu alınır. Cevap 2'dir. <br>
Bulacağımız cevapların 5'e modu alındığında kalanın 2 olması gerekmektedir. <br>
Örneğin 12'nin 5'e modunu aldığımızda kalan 2'dir. 17'nin 5'e modunu aldığımızda da kalan ikidir. <br>
Aritmetik dizi sonuçları bu şekilde sonsuza kadar devam eder.

<h2>Modüler Aritmetikte Toplama - Çıkarma - Çarpma</h2>

(A + B) mod C = (A mod C + B mod C) mod C<br>
(A - B) mod C = (A mod C - B mod C) mod C<br>
(A * B) mod C = (A mod C * B mod C) mod C<br>


<h2>Çarpma Örneği:</h2>
Source: KhanAcademy. Please visit KhanAcademy website too! Im only archiving.<br>

```
A=4, B=7, C=6 olsun
Doğrulayalım: (A * B) mod C = (A mod C * B mod C) mod C
SOL= Denklemin Sol Tarafı
SAĞ= Denklemin Sağ Tarafı
SOL= (A * B) mod C
SOL = (4 * 7) mod 6
SOL = 28 mod 6
SOL = 4
SAĞ = (A mod C * B mod C) mod C
SAĞ = (4 mod 6 * 7 mod 6) mod 6
SAĞ = (4 * 1) mod 6
SAĞ = 4 mod 6
SAĞ = 4
SOL = SAĞ = 4
```

<h2> Hızlı Modüler Üs Alma </h2>

<b>A^2 mod C = (A * A) mod C = ((A mod C) * (A mod C)) mod C</b>
