import requests
import json
# adım 1 görev ekle
def gorev_ekle(baslik, tamamlandi=False):
    """
    JSONPlaceholder'a POST isteğiyle yeni bir görev ekler.
    Gerçekte veri kaydedilmez, ancak API bize "başarılı" yanıtı döner.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    
    # Gönderilecek veri (JSON formatında)
    yeni_gorev = {
        "userId": 1,
        "title": baslik,
        "completed": tamamlandi
    }
    
    try:
        # POST isteği gönder
        response = requests.post(url, json=yeni_gorev, timeout=10)
        
        if response.status_code == 201:  # 201 = Created
            print("✅ Görev başarıyla oluşturuldu!")
            print("API'den dönen simüle edilmiş veri:")
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print(f"⚠️ Beklenmeyen durum kodu: {response.status_code}")
            
    except Exception as e:
        print(f"🚨 Hata: {e}")

#2. Adım: GET ile Tüm Görevleri Listeleme
def tum_gorevleri_getir(user_id=1):
    """Belirli bir kullanıcıya ait görevleri listeler."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            gorevler = response.json()
            print(f"\n📋 Kullanıcı {user_id} için {len(gorevler)} görev:")
            for g in gorevler[:5]:  # İlk 5'ini göster
                durum = "✅" if g["completed"] else "🔲"
                print(f"{durum} {g['title']}")
        else:
            print("❌ Görevler alınamadı.")
    except Exception as e:
        print(f"🚨 Hata: {e}")

# görev güncelleme put

def gorev_guncelle(gorev_id, yeni_baslik=None, tamamlandi=None):
    """
    Belirli bir görevi PUT ile günceller.
    JSONPlaceholder'da ID'ye göre güncelleme yapılır.
    """
    url = f"https://jsonplaceholder.typicode.com/todos/{gorev_id}"
    
    # Mevcut görevi al (isteğe bağlı, sadece gösterim için)
    mevcut = requests.get(url).json()
    
    # Güncellenmiş veri
    guncel_veri = {
        "userId": mevcut["userId"],
        "id": gorev_id,
        "title": yeni_baslik or mevcut["title"],
        "completed": tamamlandi if tamamlandi is not None else mevcut["completed"]
    }
    
    try:
        response = requests.put(url, json=guncel_veri, timeout=10)
        if response.status_code == 200:
            print("🔄 Görev güncellendi!")
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print(f"⚠️ Güncelleme başarısız: {response.status_code}")
    except Exception as e:
        print(f"🚨 Hata: {e}")

# görev silme delete

def gorev_sil(gorev_id):
    """Belirli bir görevi siler (simüle edilir)."""
    url = f"https://jsonplaceholder.typicode.com/todos/{gorev_id}"
    
    try:
        response = requests.delete(url, timeout=10)
        if response.status_code == 200:
            print(f"🗑️ Görev {gorev_id} silindi (simülasyon).")
        else:
            print(f"❌ Silme başarısız: {response.status_code}")
    except Exception as e:
        print(f"🚨 Hata: {e}")


#ana program

def main():
    print("📝 JSONPlaceholder ile Yapılacaklar Listesi Yönetimi")
    print("Bu API verileri gerçekte KAYDETMEZ, sadece simülasyon yapar.\n")
    
    while True:
        print("\n" + "="*50)
        print("1. Yeni görev ekle (POST)")
        print("2. Görevleri listele (GET)")
        print("3. Görev güncelle (PUT)")
        print("4. Görev sil (DELETE)")
        print("0. Çıkış")
        secim = input("Seçiminiz: ").strip()
        
        if secim == "1":
            baslik = input("Görev başlığı: ").strip()
            if baslik:
                gorev_ekle(baslik)
        elif secim == "2":
            user_id = input("Kullanıcı ID (varsayılan: 1): ").strip() or "1"
            tum_gorevleri_getir(int(user_id))
        elif secim == "3":
            try:
                id_ = int(input("Güncellenecek görev ID'si: "))
                baslik = input("Yeni başlık (boş bırak: değiştme): ").strip() or None
                tamam = input("Tamamlandı mı? (e/h/boş): ").strip().lower()
                if tamam == "e":
                    tamamlandi = True
                elif tamam == "h":
                    tamamlandi = False
                else:
                    tamamlandi = None
                gorev_guncelle(id_, baslik, tamamlandi)
            except ValueError:
                print("❌ Geçersiz ID.")
        elif secim == "4":
            try:
                id_ = int(input("Silinecek görev ID'si: "))
                gorev_sil(id_)
            except ValueError:
                print("❌ Geçersiz ID.")
        elif secim == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()