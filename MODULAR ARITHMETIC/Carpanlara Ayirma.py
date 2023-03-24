def carpanlar(a):
    c = a
    carpanlar=[]
    carpan=2
    if a == 0 or a <= -1:
        print("dude, what u trying? lol.")
    else:
        while a > 1:
            if a % carpan == 0:
                carpanlar.append(carpan)
                a /= carpan
            else:
                carpan += 1
        carpanlar.insert(0,1)
        bolenler=[]
        for i in range(1, c + 1):
            if c % i == 0:
                bolenler.append(i)
        print(bolenler)
        return carpanlar


print(carpanlar(int(input("Çarpanını Almak istediğiniz Sayıyı Giriniz: "))))
