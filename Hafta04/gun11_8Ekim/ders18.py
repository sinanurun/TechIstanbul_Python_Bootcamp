"""
Güvenli Nesne Yeniden Oluşturma Metodu (Sınıf Metodu)
Bu yöntem, __repr__ çıktısının sadece geliştiriciye bilgi vermesi prensibini korur ve nesne oluşturma işini sınıfın kendisinde tanımlanmış, güvenli bir fabrika (factory) metoduna bırakır.

Nasıl Çalışır?
__repr__ sadece nesnenin durumunu açıklar.

Sınıfa, dize formatındaki veriyi alıp yeni bir nesne oluşturan özel bir sınıf metodu (from_string gibi) ekleriz. Bu metot, dizeyi ayrıştırır (parse eder) ve yapıcıyı (__init__) çağırır.

Örnek
Önceki Urun sınıfını güncelleyelim. Artık eval()'a ihtiyacımız yok.
"""

class Urun:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat

    def __repr__(self):
        # Bu sadece geliştirici için bilgi amaçlı kaldı
        return f'Urun("{self.ad}", {self.fiyat})'

    # --- Alternatif Method: Güvenli Yeniden Oluşturma ---
    @classmethod
    def from_string(cls, urun_dizesi):
        """
        'Urun("Ad", Fiyat)' formatındaki bir dizeden Urun nesnesi oluşturur.
        Bu metod, dizeyi ayrıştırarak güvenliği sağlar.
        """
        import re
        
        # Düzenli ifade (Regex) ile ad ve fiyatı güvenli bir şekilde çekiyoruz
        match = re.search(r'Urun\("(.+)", (\d+)\)', urun_dizesi)
        
        if match:
            ad = match.group(1)
            fiyat = int(match.group(2))
            # Sınıfın yapıcı metodunu (cls, yani Urun.__init__) çağırarak nesneyi oluşturuyoruz
            return cls(ad, fiyat)
        else:
            raise ValueError("Geçersiz ürün dizesi formatı.")

# 1. Orijinal Nesne ve repr Çıktısı
urun_a = Urun("Mouse", 250)
urun_a_repr = repr(urun_a)
print(f"repr Çıktısı: {urun_a_repr}") # Çıktı: Urun("Mouse", 250)

# 2. Güvenli Fabrika Metodu ile yeniden oluşturma
urun_b = Urun.from_string(urun_a_repr)

print(f"Yeniden Oluşturulan Nesne Adı: {urun_b.ad}")
# Çıktı: Yeniden Oluşturulan Nesne Adı: Mouse