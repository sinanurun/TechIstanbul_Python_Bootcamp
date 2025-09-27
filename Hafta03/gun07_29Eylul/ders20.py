# HATA YÖNETİMİ - ÖRNEK 20
# Sözlük ile Veri Doğrulama

print("=== KULLANICI KAYIT SİSTEMİ ===")

# Geçerli kullanıcı adları ve şifreler
kullanici_veritabani = {
    "ahmet": "sifre123",
    "ayse": "merhaba456",
    "mehmet": "python789"
}

try:
    # Kullanıcıdan bilgileri al
    kullanici_adi = input("Kullanıcı adı: ").strip().lower()
    sifre = input("Şifre: ").strip()
    
    # Boş kontrolü
    if not kullanici_adi or not sifre:
        raise ValueError("Kullanıcı adı ve şifre boş olamaz!")
    
    # Kullanıcı adı geçerli mi kontrol et
    if kullanici_adi not in kullanici_veritabani:
        raise KeyError("Kullanıcı adı bulunamadı!")
    
    # Şifre kontrolü
    if kullanici_veritabani[kullanici_adi] != sifre:
        raise ValueError("Şifre hatalı!")
    
    # Başarılı giriş
    print(f"Hoş geldiniz {kullanici_adi}! Giriş başarılı.")
    
    # Kullanıcı bilgilerini göster
    print(f"Kullanıcı adınız: {kullanici_adi}")
    print(f"Şifre uzunluğu: {len(sifre)} karakter")
    
except ValueError as e:
    print(f"HATA: {e}")
except KeyError as e:
    print(f"HATA: {e}")
    print("Mevcut kullanıcılar:", list(kullanici_veritabani.keys()))

print("Giriş işlemi tamamlandı.")