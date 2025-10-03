# DOSYA İŞLEMLERİ - ÖRNEK 5
# Hava Durumu Veri Kaydedici (JSON)

import json
import datetime
import os

def hava_durumu_ekle():
    """Yeni hava durumu verisi ekler"""
    try:
        sehir = input("Şehir: ")
        sicaklik = float(input("Sıcaklık (°C): "))
        nem = int(input("Nem (%): "))
        durum = input("Hava durumu (güneşli, bulutlu, yağmurlu, vb.): ")
        
        # Tarih bilgisi
        simdi = datetime.datetime.now()
        tarih = simdi.strftime("%d/%m/%Y %H:%M")
        
        veri = {
            "tarih": tarih,
            "sehir": sehir,
            "sicaklik": sicaklik,
            "nem": nem,
            "durum": durum.lower()
        }
        
        # JSON dosyasına ekle
        kayitlar = []
        if os.path.exists("hava_durumu.json"):
            with open("hava_durumu.json", "r", encoding="utf-8") as dosya:
                kayitlar = json.load(dosya)
        
        kayitlar.append(veri)
        
        with open("hava_durumu.json", "w", encoding="utf-8") as dosya:
            json.dump(kayitlar, dosya, ensure_ascii=False, indent=2)
        
        print("✅ Hava durumu verisi başarıyla eklendi!")
        
    except ValueError:
        print("❌ Hata: Sıcaklık sayı, nem tam sayı olmalıdır!")
    except Exception as e:
        print(f"❌ Hata: {e}")

def sehre_gore_listele():
    """Şehre göre hava durumu kayıtlarını listeler"""
    try:
        if not os.path.exists("hava_durumu.json"):
            print("❌ Henüz hiç veri yok!")
            return
        
        with open("hava_durumu.json", "r", encoding="utf-8") as dosya:
            kayitlar = json.load(dosya)
        
        if not kayitlar:
            print("❌ Henüz hiç veri yok!")
            return
        
        sehir = input("Şehir adı: ")
        sehir_kayitlari = [k for k in kayitlar if k['sehir'].lower() == sehir.lower()]
        
        if not sehir_kayitlari:
            print(f"❌ '{sehir}' için kayıt bulunamadı!")
            return
        
        print(f"\n🌤️  {sehir.upper()} HAVA DURUMU KAYITLARI ({len(sehir_kayitlari)} kayıt)")
        print("=" * 70)
        
        for kayit in sehir_kayitlari:
            print(f"{kayit['tarih']} - {kayit['sicaklik']}°C - %{kayit['nem']} - {kayit['durum']}")
                  
    except Exception as e:
        print(f"❌ Hata: {e}")

def istatistikler():
    """Hava durumu istatistiklerini gösterir"""
    try:
        if not os.path.exists("hava_durumu.json"):
            print("❌ Henüz hiç veri yok!")
            return
        
        with open("hava_durumu.json", "r", encoding="utf-8") as dosya:
            kayitlar = json.load(dosya)
        
        if not kayitlar:
            print("❌ Henüz hiç veri yok!")
            return
        
        # İstatistikleri hesapla
        toplam_kayit = len(kayitlar)
        sicakliklar = [k['sicaklik'] for k in kayitlar]
        ortalama_sicaklik = sum(sicakliklar) / toplam_kayit
        max_sicaklik = max(sicakliklar)
        min_sicaklik = min(sicakliklar)
        
        # Şehir dağılımı
        sehirler = {}
        for kayit in kayitlar:
            sehir = kayit['sehir']
            sehirler[sehir] = sehirler.get(sehir, 0) + 1
        
        # Hava durumu dağılımı
        durumlar = {}
        for kayit in kayitlar:
            durum = kayit['durum']
            durumlar[durum] = durumlar.get(durum, 0) + 1
        
        print("\n📊 HAVA DURUMU İSTATİSTİKLERİ")
        print("=" * 40)
        print(f"Toplam kayıt: {toplam_kayit}")
        print(f"Ortalama sıcaklık: {ortalama_sicaklik:.1f}°C")
        print(f"En yüksek sıcaklık: {max_sicaklik}°C")
        print(f"En düşük sıcaklık: {min_sicaklik}°C")
        
        print("\nŞehir Dağılımı:")
        for sehir, sayi in sehirler.items():
            print(f"  {sehir}: {sayi} kayıt")
        
        print("\nHava Durumu Dağılımı:")
        for durum, sayi in durumlar.items():
            print(f"  {durum}: {sayi} kayıt")
                  
    except Exception as e:
        print(f"❌ Hata: {e}")

def son_kayitlari_goster():
    """Son 5 kaydı gösterir"""
    try:
        if not os.path.exists("hava_durumu.json"):
            print("❌ Henüz hiç veri yok!")
            return
        
        with open("hava_durumu.json", "r", encoding="utf-8") as dosya:
            kayitlar = json.load(dosya)
        
        if not kayitlar:
            print("❌ Henüz hiç veri yok!")
            return
        
        son_kayitlar = kayitlar[-5:]  # Son 5 kayıt
        
        print(f"\n🕒 SON 5 HAVA DURUMU KAYDI")
        print("=" * 70)
        
        for kayit in reversed(son_kayitlar):
            print(f"{kayit['tarih']} - {kayit['sehir']} - {kayit['sicaklik']}°C - "
                  f"%{kayit['nem']} - {kayit['durum']}")
                  
    except Exception as e:
        print(f"❌ Hata: {e}")

# Ana program
print("🌤️  HAVA DURUMU VERİ KAYDEDİCİ")
print("=" * 30)

while True:
    print("\n1. Hava Durumu Ekle")
    print("2. Şehre Göre Listele")
    print("3. Son Kayıtları Göster")
    print("4. İstatistikler")
    print("5. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        hava_durumu_ekle()
    elif secim == "2":
        sehre_gore_listele()
    elif secim == "3":
        son_kayitlari_goster()
    elif secim == "4":
        istatistikler()
    elif secim == "5":
        print("👋 Program kapatılıyor...")
        break
    else:
        print("❌ Geçersiz seçim!")

print("Hava durumu kaydedici sonlandırıldı!")