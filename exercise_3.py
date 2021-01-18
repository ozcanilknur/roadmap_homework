

class Ogrenci:

    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif

    def OgrenciBilgi(self):

        self.ogrenciSinif = input("Öğrenci Sınıfı Giriniz: ")
        self.ogrenciAdi = input("Öğrenci Adı Giriniz:")
        self.ogrenciSoyadi = input("Öğrenci Soyadı Giriniz:")
        return self.ogrenciSoyadi + " " + self.ogrenciAdi + " " + self.ogrenciSinif+". Sınıf"


class Soru:

    def __init__(self):
        while True:
            self.dogru = int(input("Öğrenci doğru sayısı : "))
            self.yanlis = int(input("Öğrenci yanlış sayısı: "))
            sorusayisi = self.yanlis+self.dogru
            if sorusayisi > 50:
                print("Lütfen 50 soruluk dogru yanlis degeri girin.")
                continue
            else:
                break

    def NetSayisi(self):

        netsonuc = self.dogru - (self.yanlis/4)
        print("Öğrenci net sayısı : ", netsonuc)
        return netsonuc

    def Hesapla(self, netsonuc):
        puan = netsonuc*2
        return puan

Soru1 = Soru()
print("\n Sonuçlar: \n" + Ogrenci("s","s","s").OgrenciBilgi())
print("Öğrenci Puanı : ", Soru1.Hesapla(Soru1.NetSayisi()))
