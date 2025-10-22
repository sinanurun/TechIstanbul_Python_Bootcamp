import os
import json
from flask import Flask, request, render_template, redirect, url_for, flash

# 📍 app.py'nin bulunduğu dizini temel al
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dosya yolları: app.py'ye göre
VERI_DOSYASI = os.path.join(BASE_DIR, 'veriler', 'kullanicilar.json')
UPLOAD_KLASORU = os.path.join(BASE_DIR, 'static', 'uploads')

# Gerekli klasörleri oluştur
os.makedirs(os.path.dirname(VERI_DOSYASI), exist_ok=True)
os.makedirs(UPLOAD_KLASORU, exist_ok=True)

# Flask uygulaması
app = Flask(__name__,
            static_folder=os.path.join(BASE_DIR, 'static'),
            template_folder=os.path.join(BASE_DIR, 'templates'))
app.secret_key = 'gizli_anahtar_123'

# ======================
# Yardımcı Fonksiyonlar
# ======================

def verileri_oku():
    """JSON dosyasını okur. Dosya yoksa, boşsa veya bozuksa boş liste döner."""
    try:
        if os.path.exists(VERI_DOSYASI):
            with open(VERI_DOSYASI, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        return []
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"UYARI: {VERI_DOSYASI} bozuk veya geçersiz. Sıfırlanıyor. Hata: {e}")
        return []

def verileri_yaz(veriler):
    """Verileri güvenli şekilde JSON dosyasına yazar."""
    with open(VERI_DOSYASI, 'w', encoding='utf-8') as f:
        json.dump(veriler, f, ensure_ascii=False, indent=2)

# ======================
# Route'lar
# ======================

@app.route('/')
def index():
    kullanicilar = verileri_oku()
    return render_template('index.html', kullanicilar=kullanicilar)

@app.route('/ekle', methods=['GET', 'POST'])
def ekle():
    if request.method == 'POST':
        ad = request.form.get('ad', '').strip()
        soyad = request.form.get('soyad', '').strip()
        resim = request.files.get('resim')

        if not ad or not soyad:
            flash("Ad ve soyad zorunludur!", "error")
            return redirect(url_for('index'))

        dosya_adi = None
        if resim and resim.filename:
            from werkzeug.utils import secure_filename
            dosya_adi = secure_filename(resim.filename)
            sayac = 1
            orijinal_ad = dosya_adi
            while os.path.exists(os.path.join(UPLOAD_KLASORU, dosya_adi)):
                name, ext = os.path.splitext(orijinal_ad)
                dosya_adi = f"{name}_{sayac}{ext}"
                sayac += 1
            resim.save(os.path.join(UPLOAD_KLASORU, dosya_adi))

        veriler = verileri_oku()
        yeni_id = max([k.get('id', 0) for k in veriler], default=0) + 1

        veriler.append({
            "id": yeni_id,
            "ad": ad,
            "soyad": soyad,
            "resim": dosya_adi
        })
        verileri_yaz(veriler)
        flash(f"{ad} {soyad} başarıyla eklendi!", "success")
        return redirect(url_for('index'))

    return redirect(url_for('index'))

@app.route('/guncelle/<int:kullanici_id>', methods=['GET', 'POST'])
def guncelle(kullanici_id):
    veriler = verileri_oku()
    kullanici = next((k for k in veriler if k.get('id') == kullanici_id), None)
    if not kullanici:
        flash("Kullanıcı bulunamadı.", "error")
        return redirect(url_for('index'))

    if request.method == 'POST':
        ad = request.form.get('ad', '').strip()
        soyad = request.form.get('soyad', '').strip()
        resim = request.files.get('resim')

        if not ad or not soyad:
            flash("Ad ve soyad zorunludur!", "error")
            return render_template('guncelle.html', kullanici=kullanici)

        eski_resim = kullanici.get('resim')
        yeni_resim_adi = eski_resim

        if resim and resim.filename:
            from werkzeug.utils import secure_filename
            dosya_adi = secure_filename(resim.filename)
            sayac = 1
            orijinal_ad = dosya_adi
            while os.path.exists(os.path.join(UPLOAD_KLASORU, dosya_adi)):
                name, ext = os.path.splitext(orijinal_ad)
                dosya_adi = f"{name}_{sayac}{ext}"
                sayac += 1

            if eski_resim:
                eski_yol = os.path.join(UPLOAD_KLASORU, eski_resim)
                if os.path.exists(eski_yol):
                    os.remove(eski_yol)

            resim.save(os.path.join(UPLOAD_KLASORU, dosya_adi))
            yeni_resim_adi = dosya_adi

        kullanici['ad'] = ad
        kullanici['soyad'] = soyad
        kullanici['resim'] = yeni_resim_adi

        verileri_yaz(veriler)
        flash(f"{ad} {soyad} başarıyla güncellendi!", "success")
        return redirect(url_for('index'))

    return render_template('guncelle.html', kullanici=kullanici)

@app.route('/sil/<int:kullanici_id>')
def sil(kullanici_id):
    veriler = verileri_oku()
    for i, k in enumerate(veriler):
        if k.get('id') == kullanici_id:
            if k.get('resim'):
                resim_yolu = os.path.join(UPLOAD_KLASORU, k['resim'])
                if os.path.exists(resim_yolu):
                    os.remove(resim_yolu)
            veriler.pop(i)
            verileri_yaz(veriler)
            flash(f"{k['ad']} {k['soyad']} silindi.", "success")
            break
    else:
        flash("Kullanıcı bulunamadı.", "error")
    return redirect(url_for('index'))

@app.route('/kullanici/<int:kullanici_id>')
def kullanici_detay(kullanici_id):
    veriler = verileri_oku()
    kullanici = next((k for k in veriler if k.get('id') == kullanici_id), None)
    if not kullanici:
        flash("Kullanıcı bulunamadı.", "error")
        return redirect(url_for('index'))
    return render_template('kullanici.html', kullanici=kullanici)

# ======================
# Uygulama Başlatma
# ======================

if __name__ == '__main__':
    app.run(debug=True)