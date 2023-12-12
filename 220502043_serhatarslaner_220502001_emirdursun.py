# Serhat Arslaner 220502043
# Emir Dursun 220502001

import time
import threading
from termcolor import *

# Dosya Okuma
gemiler=open("gemiler.csv","r",encoding="ISO-8859-9")
tırlar=open("olaylar.csv","r",encoding="ISO-8859-9")


# "gemiler.csv" düzenleme liste yapısı ve sözlük oluşturma.
gemiList=[]
for gemi in gemiler:
    gemiVeri=gemi.split(",")
    gemiVeriList=[i.strip("\n") for i in gemiVeri]
    gemiList.append(gemiVeriList)
gemiList.pop(0)

gemiDict=dict()

for gemidictt in gemiList:

    gemiDict[gemidictt[1]]=[gemidictt[0],gemidictt[2],gemidictt[3]]

# Gemi Verileri İçin Class
class Gemi():
    def __init__(self,gemiAdı):

        gemiAdıVeri=gemiDict[gemiAdı]

        self.gemiAdı=gemiAdı
        self.zaman=int(gemiAdıVeri[0])
        self.kapasite=int(gemiAdıVeri[1])
        self.ulke=gemiAdıVeri[2]

    

# Plaka Sıralama
def plaka_sıralama(x):
    return x[9:]


olaylarverisi=[]
olaylarverisi.sort(key=plaka_sıralama)


# "olaylar.csv" düzenleme liste yapısı ve sözlük oluşturma.
for tır in tırlar:
    anlıktır=tır.split(",")
    anlıktırlist=[i.strip("\n") for i in anlıktır]
    olaylarverisi.append(anlıktırlist)

olaylarverisi.pop(0)
olaylardict=dict()

for olaylar in olaylarverisi:
    if olaylar[3]=="0":
        olaylardict[(int(olaylar[0]),olaylar[1])]=[olaylar[2],30000,olaylar[5],olaylar[6]]
    else:
        olaylardict[(int(olaylar[0]),olaylar[1])]=[olaylar[2],20000,olaylar[5],olaylar[6]]



# Tır Verileri İçin Class
class Tır():
    def __init__(self,zaman,plaka):
        self.zaman=int(zaman)
        self.plaka=plaka
        veri=olaylardict[(zaman,plaka)]
        self.ulke=veri[0]
        self.kapasite=int(veri[1])
        self.yük_miktari=int(veri[2])
        self.maliyet=int(veri[3])

olaylarKeys = olaylardict.keys()
gemilerKeys = gemiDict.keys()

# istifAlanı - Yük İndirme - Bindirme İşlemleri İçin Class
class istifAlanı():
    def __init__(self):
        self.alan1 = 0
        self.alan2 = 0
        self.kapasite = 750
        self.Neverland = 0
        self.Mordor = 0
        self.Lilliputa = 0
        self.Oceania = 0

    def tırBilgileri(self,zaman,plaka,ulke,yukMiktarı,maliyet):
        self.zaman = zaman
        self.plaka = plaka
        self.ulke = ulke
        self.yukMiktarı = yukMiktarı
        self.maliyet = maliyet
        print(colored("{} Zamanında Gelen {} Plakalı Tır {} Ülkesine Gitmek Üzere {} Ton Yük İndirdi. Maliyet = {}".format(zaman,plaka,ulke,yukMiktarı,maliyet),"yellow"))

    def gemiBilgileri(self,zaman,gemiAdı,kapasite,gidecekUlke):
        self.zaman = zaman
        self.gemiAdı = gemiAdı
        self.kapasite = kapasite
        self.gidecekUlke = gidecekUlke 
        print(colored("{} Adlı Gemi {} Kapasite ile Limana Yaklaşıyor !!!!".format(gemiAdı,kapasite),"magenta"))


    def yükIndirme(self,miktar,ulke):
        self.ulke = ulke
        self.miktar = miktar
        toplamYuk = self.alan1 + self.alan2

        if miktar + toplamYuk < 1500:
            if self.ulke == "Neverland":
                self.Neverland += miktar
                if self.alan1 <= 750:
                    if self.alan1 + miktar > 750:
                        print("Yük Alan1'e Sığmadığı İçin Alan2'ye Aktarılıyor")
                        self.alan2 += miktar
                    else:
                        self.alan1 += miktar
                else:
                    print("İstif Alanı - 1 Dolu @ İstif Alanı - 2'ye Yükleniyor...")
                    if self.alan2 <= 750:
                        self.alan2 += miktar
                    else:
                        print("İstif Alanı - 2 Dolu @@@")
                        
            if self.ulke == "Mordor":
                self.Mordor += miktar
                if self.alan1 <= 750:
                    if self.alan1 + miktar > 750:
                        print("Yük Alan1'e Sığmadığı İçin Alan2'ye Aktarılıyor")
                        self.alan2 += miktar
                    else:
                        self.alan1 += miktar                   
                else:
                    print("İstif Alanı - 1 Dolu @ İstif Alanı - 2'ye Yükleniyor...")
                    if self.alan2 <= 750:
                        self.alan2 += miktar
                    else:
                        print("İstif Alanı - 2 Dolu @@@")

            if self.ulke == "Lilliputa":
                self.Lilliputa += miktar
                if self.alan1 <= 750:
                    if self.alan1 + miktar > 750:
                        print("Yük Alan1'e Sığmadığı İçin Alan2'ye Aktarılıyor")
                        self.alan2 += miktar
                    else:
                        self.alan1 += miktar
                else:
                    print("İstif Alanı - 1 Dolu @ İstif Alanı - 2'ye Yükleniyor...")
                    if self.alan2 <= 750:
                        self.alan2 += miktar
                    else:
                        print("İstif Alanı - 2 Dolu @@@")
            if self.ulke == "Oceania":
                self.Oceania += miktar 
                if self.alan1 <= 750:
                    if self.alan1 + miktar > 750:
                        print("Yük Alan1'e Sığmadığı İçin Alan2'ye Aktarılıyor")
                        self.alan2 += miktar
                    else:
                        self.alan1 += miktar
                else:
                    print("İstif Alanı - 1 Dolu @ İstif Alanı - 2'ye Yükleniyor...")
                    if self.alan2 <= 750:
                        self.alan2 += miktar
                    else:
                        print("İstif Alanı - 2 Dolu @@@")
        else:
            print("İstif-1 ve İstif-2 DOLU bekleyiniz...")

    def yükYükleme(self,gemiKapasitesi,gemiUlkesi,gemiZaman,gemiAdı):
        self.gemiAdı = gemiAdı
        self.gemiZaman = gemiZaman
        self.gemiKapasitesi = gemiKapasitesi
        self.gemiUlkesi = gemiUlkesi
        maxKapasite = gemiKapasitesi*(95/100)

        if self.gemiUlkesi == "Neverland":
            if self.Neverland > gemiKapasitesi:
                self.Neverland -= gemiKapasitesi
                self.alan1 -= gemiKapasitesi
                print(colored(" GEMİ KALKIYOR {} ÜLKESİNE GİDİYOR".format(gemiUlkesi),"green"))
                if self.alan2 > gemiKapasitesi:
                    self.alan2 -= gemiKapasitesi
       
        if self.gemiUlkesi == "Lilliputa":
            if self.Lilliputa > gemiKapasitesi:
                self.Lilliputa -= gemiKapasitesi
                self.alan1 -= gemiKapasitesi
                print(colored(" GEMİ KALKIYOR {} ÜLKESİNE GİDİYOR".format(gemiUlkesi),"green"))
                if self.alan2 > gemiKapasitesi:
                    self.alan2 -= gemiKapasitesi
        
        if self.gemiUlkesi == "Oceania":
            if self.Oceania > gemiKapasitesi:
                self.Oceania -= gemiKapasitesi
                self.alan1 -= gemiKapasitesi
                print(colored(" GEMİ KALKIYOR {} ÜLKESİNE GİDİYOR".format(gemiUlkesi),"green"))
                if self.alan2 > gemiKapasitesi:
                    self.alan2 -= gemiKapasitesi
                
       
        if self.gemiUlkesi == "Mordor":
            if self.Mordor > gemiKapasitesi:
                self.Mordor -= gemiKapasitesi
                self.alan1 -= gemiKapasitesi
                print(colored(" GEMİ KALKIYOR {} ÜLKESİNE GİDİYOR".format(gemiUlkesi),"green"))
                if self.alan2 > gemiKapasitesi:
                    self.alan2 -= gemiKapasitesi
        
        def alanKontrol():
            if self.alan1 == 0:
                print("İSTİF ALANI 1 = BOŞ")
            if self.alan2 == 0:
                print("İSTİF ALANI 2 = BOŞ")
            alanKontrol()
                      
limanSimülasyonu = istifAlanı()
# Yük İndirme Fonksiyonu
def olaylar():
    for i in olaylarKeys:
        tırS = Tır(i[0],i[1])
        limanSimülasyonu.yükIndirme(tırS.yük_miktari,tırS.ulke)
        limanSimülasyonu.tırBilgileri(tırS.zaman,tırS.plaka,tırS.ulke,tırS.yük_miktari,tırS.maliyet)       
        print(colored(("İSTİF ALANI = ","Alan 1 = ",limanSimülasyonu.alan1,"Alan - 2 = ",limanSimülasyonu.alan2),"cyan"))
        time.sleep(0.2)
# Yük Yükleme Fonksiyonu       
def gemiler():
     for j in gemilerKeys:
        gemiS = Gemi(j)
        limanSimülasyonu.gemiBilgileri(gemiS.zaman,gemiS.gemiAdı,gemiS.kapasite,gemiS.ulke)
        limanSimülasyonu.yükYükleme(gemiS.kapasite,gemiS.ulke,gemiS.zaman,gemiS.gemiAdı)
        time.sleep(1)
        
# Liman Otomasyonu Çalıştırma            
thread1 = threading.Thread(target=olaylar)
thread2 = threading.Thread(target=gemiler)
thread1.start()
thread2.start()
thread1.join()
thread2.join()


# Tır ve Gemi Bilgileri Sorgulama
secenek = input("Gemi Sorgulamak İçin = G, Tır Sorgulamak İçin = T tuşlayınız: ").lower()
if secenek == "g":
    def gemiSorgulama():
        gemiInput = input("Sorgulamak İstediğiniz Geminin Adını Giriniz: ")
        gemiBilgi = Gemi(gemiInput)
        print("Gemi Adı =",gemiBilgi.gemiAdı,"Gemi Kapasite = ",gemiBilgi.kapasite,"Gemi Ülkesi =" ,gemiBilgi.ulke,"Gemi Zaman =",gemiBilgi.zaman)


    gemiSorgulama()

if secenek == "t":
    def tırSorgulama():
        tırInput = input("Sorgulamak İstediğiniz Tırın Zamanını Giriniz: ")
        tırInput1 = input("Sorgulamak İstediğiniz Tırın Plakasını Giriniz: ")
        tırBilgi = Tır(tırInput,tırInput1)
        print("Kapasite =",tırBilgi.kapasite,"Maliyet = ",tırBilgi.maliyet,"Plaka =",tırBilgi.plaka,"ÜLKE = ",tırBilgi.ulke,"Yük Miktarı = ",tırBilgi.yük_miktari,"Zaman =",tırBilgi.zaman)
        


    tırSorgulama()
            












        



            
    












                               








        
        

    

      
    
        









