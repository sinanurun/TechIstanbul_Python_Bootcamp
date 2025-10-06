# ÖRNEK 4: Özellik Kontrolü
class Ogrenci:
    """Öğrenci sınıfı with validation"""
    
    def __init__(self, ad, yas, not_ortalamasi):
        # Özellik kontrolleri
        if not ad or not isinstance(ad, str):
            raise ValueError("Geçerli bir ad giriniz")
        
        if not isinstance(yas, int) or yas < 0 or yas > 120:
            raise ValueError("Yaş 0-120 arasında olmalıdır")
        
        if not isinstance(not_ortalamasi, (int, float)) or not_ortalamasi < 0 or not_ortalamasi > 100:
            raise ValueError("Not ortalaması 0-100 arasında olmalıdır")
        
        self.ad = ad
        self.yas = yas
        self.not_ortalamasi = not_ortalamasi
    
    def not_durumu(self):
        """Öğrencinin not durumunu değerlendirir"""
        if self.not_ortalamasi >= 90:
            return "Mükemmel"
        elif self.not_ortalamasi >= 80:
            return "Çok İyi"
        elif self.not_ortalamasi >= 70:
            return "İyi"
        elif self.not_ortalamasi >= 60:
            return "Orta"
        else:
            return "Zayıf"
    
    def yas_grubu(self):
        """Öğrencinin yaş grubunu belirler"""
        if self.yas < 12:
            return "Çocuk"
        elif self.yas < 18:
            return "Genç"
        elif self.yas < 30:
            return "Yetişkin"
        else:
            return "Olgun"

# Kullanım
try:
    ogrenci1 = Ogrenci("Ayşe", 20, 85.5)
    print(f"Ad: {ogrenci1.ad}")
    print(f"Not Durumu: {ogrenci1.not_durumu()}")
    print(f"Yaş Grubu: {ogrenci1.yas_grubu()}")
except ValueError as e:
    print(f"Hata: {e}")