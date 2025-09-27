# MODÜLLER - ÖRNEK 6
# OS Modülü - Dosya ve Dizin İşlemleri

import os

print("=== DOSYA ve DİZİN İŞLEMLERİ ===")

try:
    print("1: Mevcut Dizin Bilgisi")
    print("2: Dizin İçeriğini Listele")
    print("3: Yeni Dizin Oluştur")
    print("4: Dizin Değiştir")
    
    secim = int(input("Seçiminiz: "))
    
    if secim == 1:
        # Mevcut dizin bilgisi
        mevcut_dizin = os.getcwd()
        print(f"Mevcut çalışma dizini: {mevcut_dizin}")
        
        # Kullanıcı adı
        kullanici_adi = os.getlogin()
        print(f"Kullanıcı adı: {kullanici_adi}")
        
    elif secim == 2:
        # Dizin içeriğini listele
        dizin_yolu = input("Hangi dizinin içeriğini görmek istersiniz? (boş bırakırsanız mevcut dizin): ")
        
        if not dizin_yolu:
            dizin_yolu = "."
        
        if os.path.exists(dizin_yolu) and os.path.isdir(dizin_yolu):
            icerik = os.listdir(dizin_yolu)
            print(f"\n{dizin_yolu} dizinindeki dosya ve klasörler:")
            
            for i, item in enumerate(icerik, 1):
                tam_yol = os.path.join(dizin_yolu, item)
                if os.path.isdir(tam_yol):
                    print(f"{i}. 📁 {item}/ (klasör)")
                else:
                    print(f"{i}. 📄 {item} (dosya)")
        else:
            print("Geçersiz dizin yolu!")
            
    elif secim == 3:
        # Yeni dizin oluştur
        yeni_klasor = input("Oluşturmak istediğiniz klasör adı: ")
        
        if not os.path.exists(yeni_klasor):
            os.makedirs(yeni_klasor)
            print(f"'{yeni_klasor}' klasörü oluşturuldu.")
        else:
            print("Bu klasör zaten var!")
            
    elif secim == 4:
        # Dizin değiştir
        yeni_dizin = input("Geçmek istediğiniz dizin yolu: ")
        
        if os.path.exists(yeni_dizin) and os.path.isdir(yeni_dizin):
            os.chdir(yeni_dizin)
            print(f"Yeni çalışma dizini: {os.getcwd()}")
        else:
            print("Geçersiz dizin!")
            
    else:
        print("Geçersiz seçim!")
        
except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except PermissionError:
    print("HATA: Bu işlem için yetkiniz yok!")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Dizin işlemleri tamamlandı.")