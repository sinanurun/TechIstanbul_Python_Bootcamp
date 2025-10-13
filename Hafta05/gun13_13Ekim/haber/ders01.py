# =================================================
# Hafta 5 – Oturum 1: NewsAPI ile Haber Çekme
# API Anahtarı: 643ed8a0d4294f51b65b1c3f6c4ef56d
# =================================================

import requests
import json
from datetime import datetime

def haberleri_cek(ulke="us", kategori=None, api_key="643ed8a0d4294f51b65b1c3f6c4ef56d"):
    """
    NewsAPI'den güncel haberleri çeker.
    - ulke: Ülke kodu (örn: 'tr', 'us') → varsayılan: 'us'
    - kategori: İsteğe bağlı (business, sports, technology, vs.)
    - api_key: NewsAPI anahtarı (zaten sabit olarak verildi)
    """
    # ❗ URL'de BOŞLUK OLMAMALI
    url = "https://newsapi.org/v2/top-headlines"
    
    # İstek parametreleri
    params = {
        "country": ulke,
        "apiKey": api_key,
        "pageSize": 5  # En fazla 5 haber
    }
    if kategori:
        params["category"] = kategori

    try:
        # API'ye istek gönder
        response = requests.get(url, params=params, timeout=10)
        
        # Yanıtı kontrol et
        if response.status_code == 200:
            veri = response.json()
            
            # API'nin kendi hata mesajı var mı?
            if veri.get("status") != "ok":
                hata_mesaji = veri.get("message", "Bilinmeyen API hatası")
                print(f"❌ API Hatası: {hata_mesaji}")
                return None
            
            # Haber listesini al
            haberler = veri.get("articles", [])
            if not haberler:
                print("📰 Bu kriterlerde haber bulunamadı.")
                return None
            
            # Sonuçları ekrana yaz
            print(f"\n🗞️ {len(haberler)} güncel haber (Kaynak: NewsAPI):")
            print("-" * 60)
            
            for i, haber in enumerate(haberler, 1):
                baslik = haber.get("title", "Başlık yok")
                kaynak = haber.get("source", {}).get("name", "Bilinmeyen")
                url_haber = haber.get("url", "")
                yayin_tarihi = haber.get("publishedAt", "")[:10]  # YYYY-MM-DD
                
                print(f"{i}. {baslik}")
                print(f"   📌 Kaynak: {kaynak} | 📅 Tarih: {yayin_tarihi}")
                print(f"   🔗 {url_haber}\n")
            
            # Zaman damgası ekle ve döndür
            veri["_kayit_tarihi"] = datetime.now().isoformat()
            return veri
        
        elif response.status_code == 401:
            print("❌ API anahtarınız geçersiz veya aktif değil.")
            return None
        else:
            print(f"⚠️ HTTP Hatası: {response.status_code}")
            return None

    except requests.exceptions.ConnectionError:
        print("❌ İnternet bağlantınız yok.")
        return None
    except requests.exceptions.Timeout:
        print("⏱️ İstek zaman aşımına uğradı.")
        return None
    except Exception as e:
        print(f"🚨 Beklenmeyen hata: {e}")
        return None


def haberleri_json_kaydet(veri, dosya_adi="haber_arşivi.json"):
    """
    Haber verisini JSON dosyasına ekler (liste olarak saklar).
    """
    try:
        # Mevcut verileri oku
        with open(dosya_adi, "r", encoding="utf-8") as f:
            mevcut_veriler = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Dosya yoksa veya bozuksa boş liste başlat
        mevcut_veriler = []
    
    # Yeni veriyi listeye ekle
    mevcut_veriler.append(veri)
    
    # Güncel listeyi dosyaya yaz
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(mevcut_veriler, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Haberler '{dosya_adi}' dosyasına kaydedildi.")


# ========================
# ANA PROGRAM
# ========================
if __name__ == "__main__":
    print("📰 Güncel Haber Başlıkları Çekici (NewsAPI)")
    print("Kategoriler: business, entertainment, general, health, science, sports, technology")
    print("Çıkmak için 'q' yazın.\n")
    
    while True:
        # Ülke sabit: ABD (us) — isterseniz 'tr' yapabilirsiniz
        ulke = "us"  # veya "tr"
        
        kategori = input("Kategori girin (boş: genel haberler): ").strip().lower()
        if kategori == 'q':
            print("Çıkış yapılıyor...")
            break
        
        # Geçerli kategoriler listesi
        gecerli_kategoriler = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        if kategori and kategori not in gecerli_kategoriler:
            print("⚠️ Geçersiz kategori. Geçerli kategoriler:", ", ".join(gecerli_kategoriler))
            continue
        
        # Haberleri çek
        veri = haberleri_cek(ulke=ulke, kategori=kategori or None)
        
        # Başarılıysa JSON'a kaydet
        if veri:
            haberleri_json_kaydet(veri)