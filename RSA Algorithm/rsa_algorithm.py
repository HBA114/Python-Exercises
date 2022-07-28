# Konsol ekranini temizleyebilmek icin os kutuphanesini projeye dahil ettim.
import os
__author__ = "Hasan Basri Ayhaner"  # ismimi __author__ degiskenine atadim.
__email__ = "f181213013@ktun.edu.tr"    # okul epostami __email degiskenine atadim.
__studentNumber__ = "181213013"     # okul numarami __studentNumber__ degiskenine atadim.

# Ogrenci bilgilerimi ekrana yazdirdim.
print("Ad Soyad : {} \nOkul Numarası : {} \nE-Mail : {} \n".format(__author__, __studentNumber__, __email__))

def possibleP():    # Kullanicinin p sayisini kolay bir sekilde secebilmesi icin 10 ile 100 arasinda asal sayilarin listesini donduren fonksiyonu yazdim.
    x = []          # Kullaniciya liste seklinde veri dondurmek icin bir bos liste tanimladim
    # 10 dan 100 e kadar sayilari kontrol etmek ve uygun olan sayilari listeye eklemek icin bir dongu olusturdum.
    for i in range(10, 100):
        # Sayilarin asal olup olmadigini kontrol eden asagida yazdigim fonksiyon ile sayilari kontrol ettim ve asal olanlari listeye ekledim.
        if (isPrime(i)):
            x.append(i)
    return x        # Kullaniciya bu sayilarin listesini gonderdim.

# Kullanicinin q sayisini kolay bir sekilde secebilmesi icin 10 ile 100 arasinda asal sayilarin listesini donduren fonksiyonu yazdim.
def possibleQ(p):
    x = []          # Kullaniciya liste seklinde veri dondurmek icin bir bos liste tanimladim
    # 10 dan 100 e kadar sayilari kontrol etmek ve uygun olan sayilari listeye eklemek icin bir dongu olusturdum.
    for i in range(10, 100):
        # Sayilarin asal olup olmadigini kontrol eden asagida yazdigim fonksiyon ile sayilari kontrol ettim ve asal olanlari ve p ye esit olmayanlari listeye ekledim.
        if (isPrime(i) and i != p):
            x.append(i)
    return x        # Kullaniciya bu sayilarin listesini gonderdim.

# Kendisine parametre olarak verilen sayinin asal olup olmadigini kontrol eden ve gerekli boolean ciktiyi üreten fonksiyonu yazdim.
def isPrime(x):
    is_prime = True  # kontrol degiskenini basta dogru olarak atadim
    if x < 2:       # parametre olarak verilen sayinin asal sayi olamayacagi durumlari kontrol ettim ve gerekli ciktiyi dondurdum.
        return False
    elif x == 2:
        return True
    else:
        # 2 den baslayarak sayiya kadar olan sayilarla modunu aldim ve modu 0 olud ise yani tam boludu ise asal olmadigini belirtecek sekilde fonksiyon ciktisi dondurdum.
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break
    # sayinin asal olup olmadigini tutan degiskeni fonksiyon ciktisi olarak dondurdum.
    return is_prime

# p ve q üserinden hesaplanan totient değerinin parametre olarak alan ve muhtemel e acik anahtarlarini liste olarak donduren fonksiyonu yazdim.
def findE(totient):
    publicKeys = []     # Kullaniciya liste seklinde veri dondurmek icin bir bos liste tanimladim
    # 1 den totient degerine kadar sayilari kontrol edecek donguyu yazdim.
    for i in range(1, totient):
        # eger degerlendirilen sayi acik anahtar olabiliyor ise yani asal sayi ise listeye atadim.
        if (isPrime(i)):
            publicKeys.append(i)
    # fonksiyon ciktisi olarak muhtemel acik anahtarlari tutan listeyi dondurdum.
    return publicKeys

# e acik anahtari ve totient degerini parametre olarak alan ve d gizli anahtarini ureten fonksiyonu yazdim.
def findD(e, totient):
    # 1 den baslayip totient degerine kadar sayilari kontrol edecek donguyu yazdim.
    for i in range(1, totient):
        # d*e = 1 mod (totien) sartini saglayan sayiyi buldum ve fonksiyon ciktisi olarak dondurdum.
        if ((totient * i)+1) % e == 0:
            return (((totient * i)+1)/e)
    return 0    # d gizli anahtarinin bulunamamasi durumunda fonksiyon ciktisi olarak 0 dondurdum

def numberToText(numberList):   # sifreleme esnasında gerceklesen islem sonucu sifrelenmis metini olusturacak sayilari metin bicimine donusturen fonksiyonu yazdim.
    textList = []               # sayilardan olusan listeyi birer birer metin bicimine donusturup hafizada tutabilmek icin bos liste tanimladim.
    for i in range(len(numberList)):    # sifrelenmis metini olusturacak sayilari chr fonksiyonu ile karakter bicimine donusturdum ve listeye ekledim.
        textList.append(chr(numberList[i]))
    text = ''.join(str(item) for item in textList)  # listenin tum elemanlarini tek bir metin olarak tutabilmek icin join metodunu kullandim.
    return text                 # fonksiyon ciktisi olarak elde edilen metini dondurdum.

def textToNumberList(text):     # sifrelenmis metin userinde islem yapabilmek ve sifreyi cozebilmek icin metni sayi listesi bicimine donusturen fonksiyonu yazdim.
    numberList = []             # sayilari tutabilmek icin bos liste tanşmladim.
    for i in range(len(text)):  # verilen metinin her bir harfi icin ord metodu ile sayiya cevirdim ve listeye ekledim.
        numberList.append(ord(text[i]))
    return numberList           # sayilari tutan listeyi fonksiyon ciktisi olarak dondurdum.

def messageToCipher(msg, publicKey, n): # parametre olarak verilen metini yine parametre olarak verilen acik anahtar ve n sayisi ile sifreleyecek fonksiyonu yazdim.
    messageNumberList = []      # metini sayi listesinde donusturdugumde sayilari saklayabilmek icin bos bir liste olusturdum.
    cipherNumberList = []       # islem sonucu olan sayilarin saklayabilmek icin bos bir liste olusturdum.
    messageNumberList = textToNumberList(msg)   # daha once yazdigim textToNumberList fonksiyonu ile metni sayisal bir listeye donusturdum ve gerekli degiskene atadim.
    for i in range(len(messageNumberList)): # metnin uzunluğunda tekrar edecek donguyu yazdim.
        cipherNumberList.append(pow(messageNumberList[i], publicKey, n))    # metnin sayisal her bir degerini gerekli isleme tabi tutarak sonucu sifrelenmis sayilari tutan listeye ekledim
    cipherMessage = numberToText(cipherNumberList)      # sifrelenmis sayilari tutan listeyi numberToText() fonksiyonu ile metinsel bicime donusturdum.
    return cipherMessage    # fonksiyon ciktisi olarak sifrelenmis metini dondurdum

def cipherToMessage(cipherText, privateKey, n): # parametre olarak verilen sifrelenmis metini yine parametre olarak verilen gizli anahtar ve n sayisi ile cozumleyecek fonksiyonu yazdim.
    cipherNumberList = []       # sifrelenmis metini sayi listesinde donusturdugumde sayilari saklayabilmek icin bos bir liste olusturdum.
    messageNumberList = []      # cozumleme islemi sonucu olan sayilarin saklayabilmek icin bos bir liste olusturdum.
    cipherNumberList = textToNumberList(cipherText) # daha once yazdigim textToNumberList fonksiyonu ile sifreli metni sayisal bir listeye donusturdum ve gerekli degiskene atadim.
    for i in range(len(cipherNumberList)):  # sifreli metnin uzunluğunda tekrar edecek donguyu yazdim.
        messageNumberList.append(pow(cipherNumberList[i], privateKey, n))   # sifreli metnin sayisal her bir degerini gerekli isleme tabi tutarak sonucu cozumlenmis sayilari tutan listeye ekledim
    msg = numberToText(messageNumberList)   # cozumlenmis sayilari tutan listeyi numberToText() fonksiyonu ile metinsel bicime donusturdum.
    return msg      # fonksiyon ciktisi olarak cozumlenmis metini dondurdum.


def variableControl(p, q, e):   # kullanicinin islemleri secmesinde siralamayi kolay yonetebilmek icin degiskenlerin atamasinin yapilip yapilmadigini kontrol edecek fonksiyonu yazdim.
    if (p == 0 or q == 0 or e == 0):    # gerekli degerlerin secimi yapilmamis ise sifreleme islemi yapilamayacagindan islem akisini durduracak true degerini dondurdum.
        return True
    else:       # aksi durumda sifreleme islemlerinin yapilmasina engel teskil edilmediginden false dondurerek oradaki islemlerin devam etmesini sagladim.
        return False


def clearConsole():     # islemlerden sonra konsol ekraninin temizlenmesi icin isletim sistemi veya console, command propmt, bash, zsh gibi ortamlarda calisacak temizleme fonksiyonunu yazdim.
    if (os.name == "nt"):   # isletim sitemi veya konsol'un nt yani windows türü oldugu durumlarda cls komutunu kullandim.
        os.system("cls")
        return 0
    elif (os.name == "posix"):  # isletim sisteminin posix tabanli oldugu veya bash, zsh, terminal gibi konsollarda calisacak clear komutunu kullandim
        os.system("clear")
        return 0
    else:               # daha onceki sartlara uymayan konsollarda hangi komut ile temizleme yapacagimi bilmedigimi print fonksiyonu ile kullaniciya bildirdim
        print("I do not know how to clean your console.")


if __name__ == "__main__":      # programin main fonksiyonunu yazdim.
    p = 0
    q = 0
    e = 0                       # p, q, e, d, n ve totient gibi sifrelemede kullanilacak degiskenleri tanimladim ve 0 atadim.
    d = 0
    n = 0
    totient = 0
    while True:                 # kullanici islem yapmaya devam ettigi surece devam edecek donguyu kurdum.
        try:                    # try-except yapisi ile hata olusabilecek kodu cevreledim ve hata olusmasi durumunda kullaniciya bildirerek yeninden girmesi icin devam edilmesini sagladim.
            selectedProcess = int(
                input("1-Anahtarlari sec.\n2-Mesaj sifrele ve sifreyi coz\n3-Cikis\n")) # Kullaniciya islem secenegi sundum ve islem secmesini istedim.
        except ValueError:      # kullanicinin hatali deger girisi uzerine olusabilecek hatalari except ile yakaladim ve kullanin yeniden secim yapmasi icin basa dondurdum.
            print('Lutfen gecerli bir deger giriniz!\n')
            input('Devam Etmek icin Enter\'a basin...')
            clearConsole()      # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
            continue

        if selectedProcess == 1:    # kullanicinin 1 numarali anahtarlarin secildigi islemi secmesi durumunda calisacak olan fonksiyonlari burada yazdim.
            pList = possibleP()     # daha once yazdigim fonksiyon ile kullanicinin p sayisini kolay bir sekilde secebilmesi icin 10 ile 100 arasinda asal sayilarin listesini bir listeya atadim
            while True:             # kullanici dogru secim yapana kadar devam edecek bir dongu kurdum
                print(pList)
                try:                # kullanicinin klavyeden hatali giris yapmasi ile olusabilecek hatanin kontrol edilebilmesi icin try-except yapisi kurdum
                    p = int(input(
                        "Yukaridaki listeden 1. asal sayiyi(p) giriniz.(Buyuk sayilar daha guvenlidir)\n"))
                except ValueError:  # kullanicinin hatali girdigi durumda kullaniciyi uyararak tekrar girmesi icin yeniden sayi secmesini istedim
                    print('Lutfen gecerli bir deger giriniz!\n')
                    input('Devam Etmek icin Enter\'a basin...')
                    clearConsole()  # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
                    continue
                if (p in pList):    # secilen sayinin secilebilir oldugundan emin olduktan sonra islemlere devam edilmesi icin break ile donguyu kirdim.
                    break
                else:
                    clearConsole()  # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
                    print("Hatali giris lutfen listeden 1. asal sayiyi(p) giriniz")
            qList = possibleQ(p)    # daha once yazdigim fonksiyon ile kullanicinin q sayisini kolay bir sekilde secebilmesi icin 10 ile 100 arasinda p'yi icermeyen asal sayilarin listesini bir listeya atadim
            while True:             # kullanici dogru secim yapana kadar devam edecek bir dongu kurdum
                print(qList)
                try:                # kullanicinin klavyeden hatali giris yapmasi ile olusabilecek hatanin kontrol edilebilmesi icin try-except yapisi kurdum
                    q = int(input(
                        "Yukaridaki listeden 2. asal sayiyi(q) giriniz.(Buyuk sayilar daha guvenlidir)\n"))
                except ValueError:  # kullanicinin hatali girdigi durumda kullaniciyi uyararak tekrar girmesi icin yeniden sayi secmesini istedim
                    print('Lutfen gecerli bir deger giriniz!\n')
                    input('Devam Etmek icin Enter\'a basin...')
                    clearConsole()  # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
                    continue
                if (q in qList):    # secilen sayinin secilebilir oldugundan emin olduktan sonra islemlere devam edilmesi icin break ile donguyu kirdim.
                    break
                else:
                    clearConsole()  # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
                    print("Hatali giris lutfen listeden 2. asal sayiyi(q) giriniz")
            n = p * q               # secilen p ve q sayilarinin carpimindan olusan n degerini hesaplayarak bir degiskene atadim.
            totient = (p - 1) * (q - 1) # secilen p ve q sayilarinin birer eksiginin carpimindan olusan totient degerini bir degiskene atadim.
            eList = findE(totient)      # daha once yazdigim fonksiyon ile muhtemel tum acik anahtarlari kullanicinin secmesi icin bir listeye atadim.
            while True:             # kullanici dogru secim yapana kadar devam edecek bir dongu kurdum
                print(eList)        # muhtemel tum acik anahtarlari tutan listeyi ekrana yazdirdim.
                try:                # kullanicinin klavyeden hatali giris yapmasi ile olusabilecek hatanin kontrol edilebilmesi icin try-except yapisi kurdum
                    e = int(input("Yukaridaki listeden acik anahtarinizi seciniz...\n"))
                except ValueError:  # kullanicinin hatali girdigi durumda kullaniciyi uyararak tekrar girmesi icin yeniden sayi secmesini istedim
                    print('Lutfen gecerli bir deger giriniz!\n')
                    input('Devam Etmek icin Enter\'a basin...')
                    clearConsole()  # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
                    continue
                if (e in eList):    # secilen sayinin secilebilir oldugundan emin olduktan sonra islemlere devam edilmesi icin break ile donguyu kirdim.
                    break
                else:
                    print("Hatali giris lutfen listeden acik anahtar seciniz")
            d = int(findD(e, totient))  # belirlenen e acik anahtari ve totienti parametre olarak alan ve gizli anahtari hesaplayan fonksiyon ile gizli anahtri hesaplayip gerekli degiskene atadim.
            print("Gizli anahtarinizi kimse ile paylasmayiniz : {}".format(d))
            input('Devam Etmek icin Enter\'a basin...')
            clearConsole()      # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
            continue

        if selectedProcess == 2:    # kullanicinin 2 numarali metin sifreleme ve sifre cozme islemini secmesi durumunda calisacak olan fonksiyonlari burada yazdim.
            if (variableControl(p, q, e)):
                print("Lutfen once anahtar belirleyiniz!")
                input('Devam Etmek icin Enter\'a basin...')
                clearConsole()  # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
                continue
            message = input("Sifrelenecek metini giriniz...\n") # Kullanicidan sifrelemek istedigi metni girmesini istedim.
            cipherText = messageToCipher(msg=message, publicKey=e, n=n) # kullanicinin girdigi metni parametre olarak alan messageToCipher fonksiyonu ile sifreleyerek ekrana yazdirdim.
            print("Sifrelenmis metin : {}".format(cipherText))
            messageFromCipher = cipherToMessage(
                cipherText=cipherText, privateKey=d, n=n)   # sifrelenmis metini parametre olarak alan cipherToMessage fonksiyonu ile sifrelenen metni cozumledim ve ekrana yazdirdim.
            print("Cozulmus metin : {}".format(messageFromCipher))
            input('Devam Etmek icin Enter\'a basin...')
            clearConsole()      # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim
            continue

        if selectedProcess == 3:    # kullanicinin 3 numarali cikis islemini secmesi durumunda exit fonksiyonu ile programi sonlandirdim.
            exit()
        if selectedProcess != 1 or selectedProcess != 2 or selectedProcess != 3:    # gecersiz islem numarasi girilmesi durumunda kullanicinin uyarilmasini ve programin yeniden secim ekranina donmesini sagladim.
            print('Lutfen gecerli bir deger giriniz!\n')
            input('Devam Etmek icin Enter\'a basin...')
            continue
        input('Devam Etmek icin Enter\'a basin...')
        clearConsole()      # daha once yazdigim ekran temizleyici fonksiyon ile ekrani temizledim