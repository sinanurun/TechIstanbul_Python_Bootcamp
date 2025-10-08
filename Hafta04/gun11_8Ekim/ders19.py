"""
Veri Serileştirme (JSON veya Pickle)
Bu, veriyi depolama, ağ üzerinden gönderme veya kalıcı hale getirme (persistence) gibi durumlarda kullanılan en yaygın ve güvenli yaklaşımdır.

a) JSON (JavaScript Object Notation)
JSON, veriyi yapılandırılmış, okunabilir bir metin formatına dönüştürmek için idealdir.

Serileştirme (Serialization): Nesneyi JSON'a dönüştürmek için özel bir metot (to_dict gibi) tanımlanır.

De-serileştirme (Deserialization): JSON verisini alıp nesneyi yeniden oluşturmak için bir sınıf metodu (from_json gibi) tanımlanır.

Örnek: JSON Kullanımı
"""

import json

class UrunJSON:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat

    def to_dict(self):
        """Nesneyi güvenli bir dictionary'ye (sözlüğe) dönüştürür."""
        return {"ad": self.ad, "fiyat": self.fiyat}

    @classmethod
    def from_dict(cls, veri_sozluk):
        """Dictionary'den nesneyi yeniden oluşturur."""
        return cls(veri_sozluk["ad"], veri_sozluk["fiyat"])

# 1. Orijinal Nesne
urun_c = UrunJSON("Monitör", 4000)

# 2. Serileştirme (Nesne -> JSON Metni)
urun_json = json.dumps(urun_c.to_dict())
print(f"JSON Çıktısı: {urun_json}")
# Çıktı: JSON Çıktısı: {"ad": "Monitör", "fiyat": 4000}

# 3. De-serileştirme (JSON Metni -> Yeni Nesne)
urun_dict = json.loads(urun_json) # JSON metnini sözlüğe çevir
urun_d = UrunJSON.from_dict(urun_dict) # Sözlükten nesneyi oluştur

print(f"Yeniden Oluşturulan Nesne Fiyatı: {urun_d.fiyat}")
# Çıktı: Yeniden Oluşturulan Nesne Fiyatı: 4000