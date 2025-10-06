#class içersinde tanımlanabilen tüm methodlar ile ilgili ortak önrke

class Calisan:
    zam_orani = 1.1  # class değişkeni

    def __init__(self, ad, maas):
        self.ad = ad
        self.maas = maas

    def maas_goster(self):   # instance method
        print(f"{self.ad} maaşı: {self.maas}₺")

    @classmethod
    def zam_yap(cls, oran):
        cls.zam_orani = oran
        print(f"Yeni zam oranı: {cls.zam_orani}")

    @staticmethod
    def bilgi():
        print("Bu sınıf çalışan maaşlarını yönetir.")

# Kullanım
Calisan.bilgi()                # static method
Calisan.zam_yap(1.2)           # class method
c1 = Calisan("Ahmet", 10000)
c1.maas_goster()               # instance method
