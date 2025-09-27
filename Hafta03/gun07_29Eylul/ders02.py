# HATA YÖNETİMİ - ÖRNEK 2
# Tip Dönüşüm Hatası Yönetimi

"""
Bu program, kullanıcıdan yaş bilgisi alıp doğum yılını hesaplar.
Kullanıcı sayı yerine metin girerse, program hata verip sonlanmaz,
ona uygun bir mesaj gösterir ve tekrar deneme şansı verir.
"""

print("=== DOĞUM YILI HESAPLAMA ===")

while True:
    try:
        # Kullanıcıdan yaş bilgisini alıyoruz
        yas = int(input("Yaşınızı girin: "))
        
        # Doğum yılını hesaplıyoruz (basitçe 2024'ten çıkarıyoruz)
        dogum_yili = 2024 - yas
        
        # Sonucu ekrana yazdırıyoruz
        print(f"Doğum yılınız: {dogum_yili}")
        break  # Doğru giriş yapıldı, döngüden çık
        
    except ValueError:
        # Eğer kullanıcı sayı yerine metin girerse
        print("HATA: Lütfen sadece sayı girin! (Örnek: 25)")
        
        # Kullanıcıya çıkış seçeneği sunuyoruz
        devam = input("Tekrar denemek için 'e', çıkmak için 'h' yazın: ")
        if devam.lower() == 'h':
            print("Program sonlandırıldı.")
            break

print("Teşekkür ederiz!")