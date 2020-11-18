

class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif

    def OgrenciBilgi(self):

        self.ogrenciSinif = input("Ogrenci Sinifi: ")
        self.ogrenciAdi = input("Ogrenci Adi:")
        self.ogrenciSoyadi = input("Ogrenci Soyadi:")
        return self.ogrenciSoyadi +" "+ self.ogrenciAdi +" "+ self.ogrenciSinif+". sinif"


class Soru:

    def NetSayisi(self):
        while(True):
            self.dogru = int(input("Dogru Sayisi:"))
            self.yanlis = int(input("Yanlis Sayisi:"))
            if self.dogru+self.yanlis > 100:
                print("Lütfen 100 soruluk dogru yanlis degeri girin.")
                Soru().NetSayisi()

            else:
                global netsonuc
                netsonuc = self.dogru - (self.yanlis/4)
            return int(netsonuc)

    def Hesapla(self):
        puan = netsonuc*10
        return int(puan)



print("\n Sonuclar: \n ", Ogrenci("s","s","s").OgrenciBilgi(), "Net:" ,Soru().NetSayisi(), "Puan:", Soru().Hesapla())








