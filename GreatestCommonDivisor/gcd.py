import os

list = []
dizi = []

def findGCD(a,b):
    if a < b:
        a,b = b,a
    if a%b == 0:
        return b
    else:
        return findGCD(b,a%b)

def Euclidian(a,b):     # findGCD(a,b) = ax + by olacaktir.
    if a < b:
        a,b = b,a
    ana = a
    bolum = b
    kalan = ana%bolum
    if kalan == 0:
        dizi.append(ana)
        dizi.append(ana//bolum)
        list.append(ana//bolum)
        dizi.append(bolum)
        dizi.append(kalan)
        return a,b
    dizi.append(ana)
    dizi.append(ana//bolum)
    list.append(ana//bolum)
    dizi.append(bolum)
    dizi.append(kalan)
    print('{} = {} * {} + {}'.format(ana,ana//bolum,bolum,kalan))
    return Euclidian(bolum,kalan)

def EuclidianReverse(dizi,a,b,count):
    if count == -1:
        count = 1
    else: count = -1
    i = -1
    x = 0
    y = -1
    while -i <= len(dizi)-3:
        print('{} = {} - {} * {}'.format(dizi[i],dizi[i-3],dizi[i-2],dizi[i-1]))
        x += 1
        i = i - 4

def _findXY(x,y,list,index):
    index = index - 1
    if index == 0:
        return (y-(list[index] * x)),x
    else:
        x,y = _findXY((y-(list[index] * x)),x,list,index)
        return x,y

def getAB():
    a = int(input('a sayisini giriniz...\n'))
    b = int(input('b sayisini giriniz...\n'))
    if b < a:
        a,b = b,a
    return a,b

while True:
        os.system('CLS')
        print('Islemler:')
        print('1: gcd(a,b)\'yi Hesapla.')
        print('2: gcd(a,b) = ax + by\'yi Hesapla.')
        print('3: Cikis.',end='\n\n')
        try:
           secim = int(input('Islem no giriniz...\n')) # "gcd için 1'e, gcd = ax + by formunda yazdirmak icin 2'ye, Cikis icin 3'e basiniz.\n"
        except ValueError:
            print('Lutfen gecerli bir deger giriniz!\n')
            input('Devam Etmek icin Enter\'a basin...')
            continue
        list.clear()
        dizi.clear()
        if secim == 1:
            a,b = getAB()
            print('gcd({},{}) = {}'.format(a,b,findGCD(a,b)))
            input('Devam Etmek icin Enter\'a basin...')
            continue
        if secim == 2:
            a,b = getAB()
            print()
            Euclidian(a,b)
            print()
            EuclidianReverse(dizi,a,b,1)
            print()
            x,y = _findXY(0,1,list,len(list))
            print('gcd({},{}) = {}'.format(a,b,findGCD(a,b)))
            print('gcd({},{}) = {} * {} + {} * {}'.format(a,b,x,a,y,b))
            input('Devam Etmek icin Enter\'a basin...')
            continue
        if secim == 3:
            exit()
        if secim != 1 or secim != 2 or secim != 3:
            print('Lutfen gecerli bir deger giriniz!\n')
            input('Devam Etmek icin Enter\'a basin...')
            continue

