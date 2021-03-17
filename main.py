def kucukharf(sifre):
    kucukListe=['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z','w','x','q']
    for harf in sifre :
         for kontrolHarf in kucukListe:
             if harf == kontrolHarf:
                  return True
    return False

def buyukHarf(sifre):
    buyukListe=['A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J','K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z','W','X','Q']
    for harf in sifre:
         for kontrolHarf in buyukListe:
             if harf == kontrolHarf:
                  return True
    return False

def sayi(sifre):
    sayiListe=['0','1','2','3','4','5','6','7','8','9']
    for harf in sifre:
         for kontrolHarf in sayiListe:
             if harf == kontrolHarf:
                  return True
    return False

def kontrol(sifre):
    isKucuk=kucukharf(sifre)
    isBuyuk=buyukHarf(sifre)
    isSayi=sayi(sifre)

    if len(sifre)>8 and len(sifre)<15:
        uzunluk=True
    else:
        uzunluk=False
    if isBuyuk==True and isKucuk==True and uzunluk== True and isSayi==True:
        print("Şifreniz güçlü bir şifredir")
    else:
        print("Şifreniz zayıf bir şifre")
        print("Güçlü şifre için"
              "1-En az 1 büyük harf bulundurmak"
              "2-En az 1 küçük harf bulundurmak"
              "3-En az 1 sayı bulundurmak"
              "4-En az 8 en fazla 15 karakterden oluşması")
kullaniciSifre=input("Şifrenizi giriniz:")
kontrol(kullaniciSifre)# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
