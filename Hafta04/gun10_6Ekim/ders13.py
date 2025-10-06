class Fatura():
    baslik = "Halil Pazarlama"
    odeme = True
    icerik = {}
    def __init__(self,mAdi,vergiNo,tarih):
        self.mAdi = mAdi
        self.vergiNo = vergiNo
        self.tarih = tarih
        self.tutar = 0

    def urun_ekle(self):
        urun_adi = input("ürün adı giriniz")
        urun_adeti = int(input("Adet"))
        urun_fiyati = int(input("Birim Fiyati"))
        urun_tutar = urun_adeti * urun_fiyati
        self.icerik[urun_adi] = [urun_adeti,urun_fiyati,urun_tutar]
        self.tutar += urun_tutar
        print(self.icerik[urun_adi]," sepete eklendi")
        return self.fatura_tutari()

    def urun_cikar(self):
        urun_adi = input("ürün adı giriniz")
        urun_tutar = self.icerik[urun_adi][2]
        self.tutar -= urun_tutar
        print(self.icerik[urun_adi]," sepetten Silindi")
        del self.icerik[urun_adi]
        return self.fatura_tutari()

    def fatura_tutari(self):
        print("Güncel fatura Tutarı", self.tutar)
        return self.tutar


musteri = Fatura("Hale",1545454,2024)
musteri.urun_ekle()
