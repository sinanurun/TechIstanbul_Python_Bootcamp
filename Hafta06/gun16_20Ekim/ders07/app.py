"""
Jinja2 etiketleri:
{{ ... }} → Değişken yazdırma
{% ... %} → Mantıksal yapılar (if, for, vs.)
{# ... #} → Yorum satırı
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    yazilar = [
        {"baslik": "Flask Nedir?", "icerik": "Flask, hafif bir Python web framework'üdür."},
        {"baslik": "Jinja2 Öğreniyorum", "icerik": "Şablon motoru çok kullanışlı!"},
        {"baslik": "Sanal Ortam", "icerik": "Bağımlılıkları izole etmek için harika."}
    ]
    return render_template('index.html', yazilar=yazilar)

@app.route('/profil')
def profil():
    kullanici = {"ad": "Elif", "aktif": True}
    return render_template('profil.html', kullanici=kullanici)

@app.route('/kullanicilar')
def kullanicilar():
    liste = [
        {"ad": "Ahmet", "aktif": True},
        {"ad": "Mehmet", "aktif": False},
        {"ad": "Ayşe", "aktif": True}
    ]
    return render_template('kullanicilar.html', kullanicilar=liste)

if __name__ == "__main__":
    app.run(debug=True)