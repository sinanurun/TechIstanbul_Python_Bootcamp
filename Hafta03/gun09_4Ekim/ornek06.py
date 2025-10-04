"""
KULLANIM SENARYOSU: 
Bu örnek, dosya işlemlerinde yedekleme yapmanın önemini gösterir.
Bir dosyayı değiştirmeden önce yedek almak, veri kaybını önler.

NEDEN BU ÖRNEK:
- with deyimi kullanımı
- Dosya varlık kontrolü
- Hata yönetimi
- Zaman damgası kullanımı
"""

import os
import datetime

def yedekle_ve_yaz(dosya_adi, yeni_icerik):
    """Dosyayı yedekledikten sonra yeni içerik yazar"""
    
    # Eğer dosya varsa yedekle
    if os.path.exists(dosya_adi):
        # Zaman damgası ile yedek dosya adı oluştur
        zaman = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        isim, uzanti = os.path.splitext(dosya_adi)
        yedek_adi = f"{isim}.backup_{zaman}{uzanti}"

        
        try:
            # Orijinal dosyayı yedekle
            with open(dosya_adi, 'r', encoding='utf-8') as orijinal:
                with open(yedek_adi, 'w', encoding='utf-8') as yedek:
                    yedek.write(orijinal.read())
            print(f"✅ Yedek oluşturuldu: {yedek_adi}")
            
        except Exception as e:
            print(f"❌ Yedekleme hatası: {e}")
            return False
    
    # Yeni içeriği yaz
    try:
        with open(dosya_adi, 'w', encoding='utf-8') as dosya:
            dosya.write(yeni_icerik)
        print(f"✅ Dosya güncellendi: {dosya_adi}")
        return True
        
    except Exception as e:
        print(f"❌ Yazma hatası: {e}")
        return False

# Kullanım örneği
icerik = """Bu güncellenmiş içeriktir.
Dosya işlemleri önemlidir.
Her zaman yedek almayı unutmayın!"""

yedekle_ve_yaz("onemli_notlar.txt", icerik)