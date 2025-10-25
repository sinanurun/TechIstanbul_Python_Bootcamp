# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Kategori, Kitap
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gizli-anahtar'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "site.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ORM nesnesini uygulamaya bağla
db.init_app(app)

# Uygulama bağlamında veritabanını oluştur
with app.app_context():
    db.create_all()

# --- Ana Sayfa: Tüm kitapları ve kategorileri listeler ---
@app.route('/')
def index():
    kitaplar = Kitap.query.all()
    kategoriler = Kategori.query.all()
    return render_template('index.html', kitaplar=kitaplar, kategoriler=kategoriler)

# --- KATEGORİ İŞLEMLERİ ---

@app.route('/kategori/ekle', methods=['GET', 'POST'])
def kategori_ekle():
    if request.method == 'POST':
        ad = request.form['ad'].strip()
        if ad:
            if Kategori.query.filter_by(ad=ad).first():
                flash('Bu kategori zaten mevcut!', 'danger')
            else:
                yeni_kategori = Kategori(ad=ad)
                db.session.add(yeni_kategori)
                db.session.commit()
                flash('Kategori eklendi!', 'success')
                return redirect(url_for('index'))
        else:
            flash('Kategori adı boş olamaz!', 'warning')
    return render_template('kategori_ekle.html')

@app.route('/kategori/guncelle/<int:id>', methods=['GET', 'POST'])
def kategori_guncelle(id):
    kategori = Kategori.query.get_or_404(id)
    if request.method == 'POST':
        yeni_ad = request.form['ad'].strip()
        if yeni_ad:
            if Kategori.query.filter(Kategori.ad == yeni_ad, Kategori.id != id).first():
                flash('Bu kategori adı zaten kullanılıyor!', 'danger')
            else:
                kategori.ad = yeni_ad
                db.session.commit()
                flash('Kategori güncellendi!', 'success')
                return redirect(url_for('index'))
        else:
            flash('Kategori adı boş olamaz!', 'warning')
    return render_template('kategori_guncelle.html', kategori=kategori)

@app.route('/kategori/sil/<int:id>')
def kategori_sil(id):
    kategori = Kategori.query.get_or_404(id)
    # Kitapları otomatik siler (cascade sayesinde)
    db.session.delete(kategori)
    db.session.commit()
    flash('Kategori ve bağlı kitapları silindi!', 'success')
    return redirect(url_for('index'))

# --- KİTAP İŞLEMLERİ ---

@app.route('/kitap/ekle', methods=['GET', 'POST'])
def kitap_ekle():
    kategoriler = Kategori.query.all()
    if request.method == 'POST':
        baslik = request.form['baslik'].strip()
        yazar = request.form['yazar'].strip()
        kategori_id = request.form.get('kategori_id')
        if baslik and yazar and kategori_id:
            yeni_kitap = Kitap(baslik=baslik, yazar=yazar, kategori_id=int(kategori_id))
            db.session.add(yeni_kitap)
            db.session.commit()
            flash('Kitap eklendi!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Tüm alanlar doldurulmalıdır!', 'warning')
    return render_template('kitap_ekle.html', kategoriler=kategoriler)

@app.route('/kitap/guncelle/<int:id>', methods=['GET', 'POST'])
def kitap_guncelle(id):
    kitap = Kitap.query.get_or_404(id)
    kategoriler = Kategori.query.all()
    if request.method == 'POST':
        baslik = request.form['baslik'].strip()
        yazar = request.form['yazar'].strip()
        kategori_id = request.form.get('kategori_id')
        if baslik and yazar and kategori_id:
            kitap.baslik = baslik
            kitap.yazar = yazar
            kitap.kategori_id = int(kategori_id)
            db.session.commit()
            flash('Kitap güncellendi!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Tüm alanlar doldurulmalıdır!', 'warning')
    return render_template('kitap_guncelle.html', kitap=kitap, kategoriler=kategoriler)

@app.route('/kitap/sil/<int:id>')
def kitap_sil(id):
    kitap = Kitap.query.get_or_404(id)
    db.session.delete(kitap)
    db.session.commit()
    flash('Kitap silindi!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)