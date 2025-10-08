"""
KALITIM TEMEL KAVRAMLARI:
- Üst sınıf (Parent class): Temel sınıf
- Alt sınıf (Child class): Üst sınıftan türeyen sınıf
- super(): Üst sınıfın metotlarına erişim
"""

# Örnek 1: Temel Kalıtım Örneği
class Hayvan:
    """Hayvanların genel özelliklerini temsil eden üst sınıf"""
    
    def __init__(self, isim, yas, tur):
        self.isim = isim
        self.yas = yas
        self.tur = tur
        self.canli = True
    
    def ses_cikar(self):
        """Hayvanın ses çıkarması"""
        print(f"{self.isim} ses çıkarıyor...")
    
    def uyu(self):
        """Hayvanın uyuması"""
        print(f"{self.isim} uyuyor... Zzz")
    
    def bilgileri_goster(self):
        """Hayvanın bilgilerini gösterir"""
        print(f"\n--- {self.tur} ---")
        print(f"İsim: {self.isim}")
        print(f"Yaş: {self.yas}")
        print(f"Canlı: {'Evet' if self.canli else 'Hayır'}")

class Kedi(Hayvan):
    """Kedi sınıfı - Hayvan sınıfından kalıtım alır"""
    
    def __init__(self, isim, yas, goz_rengi):
        # Üst sınıfın yapıcı metodunu çağır
        super().__init__(isim, yas, "Kedi")
        self.goz_rengi = goz_rengi
        self.tirmalama_gucu = 5
    
    def ses_cikar(self):
        """Kedinin ses çıkarması - Method overriding"""
        print(f"{self.isim} miyavlıyor: Miyavvv!")
    
    def tirmala(self):
        """Kedinin tırmalama yeteneği"""
        print(f"{self.isim} tırmalıyor! Güç: {self.tirmalama_gucu}")
    
    def bilgileri_goster(self):
        """Kedi bilgilerini gösterir - Method overriding"""
        super().bilgileri_goster()  # Üst sınıfın metodunu çağır
        print(f"Göz Rengi: {self.goz_rengi}")
        print(f"Tırmalama Gücü: {self.tirmalama_gucu}")

class Kopek(Hayvan):
    """Köpek sınıfı - Hayvan sınıfından kalıtım alır"""
    
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas, "Köpek")
        self.cins = cins
        self.egitim_seviyesi = 1
    
    def ses_cikar(self):
        """Köpeğin ses çıkarması - Method overriding"""
        print(f"{self.isim} havlıyor: Hav hav!")
    
    def kuyruk_salla(self):
        """Köpeğin kuyruk sallama yeteneği"""
        print(f"{self.isim} mutlu bir şekilde kuyruk sallıyor!")
    
    def egitim_ver(self):
        """Köpeğe eğitim verme"""
        self.egitim_seviyesi += 1
        print(f"{self.isim} eğitim aldı! Yeni seviye: {self.egitim_seviyesi}")
    
    def bilgileri_goster(self):
        """Köpek bilgilerini gösterir - Method overriding"""
        super().bilgileri_goster()
        print(f"Cins: {self.cins}")
        print(f"Eğitim Seviyesi: {self.egitim_seviyesi}")

# Kalıtım kullanımı
print("=== KALITIM ÖRNEĞİ: HAYVANLAR ===")

# Hayvan nesneleri oluşturma
kedi = Kedi("Pamuk", 2, "Yeşil")
kopek = Kopek("Karabaş", 3, "Golden Retriever")

# Metotları kullanma
kedi.bilgileri_goster()
kedi.ses_cikar()
kedi.tirmala()
kedi.uyu()

print("\n" + "="*40)

kopek.bilgileri_goster()
kopek.ses_cikar()
kopek.kuyruk_salla()
kopek.egitim_ver()
kopek.egitim_ver()

# isinstance kontrolü
print(f"\n--- isinstance Kontrolü ---")
print(f"kedi Kedi sınıfı mı? {isinstance(kedi, Kedi)}")
print(f"kedi Hayvan sınıfı mı? {isinstance(kedi, Hayvan)}")
print(f"kedi Kopek sınıfı mı? {isinstance(kedi, Kopek)}")

# issubclass kontrolü
print(f"\n--- issubclass Kontrolü ---")
print(f"Kedi, Hayvan'dan türedi mi? {issubclass(Kedi, Hayvan)}")
print(f"Kopek, Hayvan'dan türedi mi? {issubclass(Kopek, Hayvan)}")