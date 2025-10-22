from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

app.secret_key = 'çok_gizli_bir_anahtar_123!' #form eklediğimiz zaman


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hakkimda')
def about():
    return render_template('about.html')

@app.route('/kullanici/<isim>')
def user(isim):
    return render_template('user.html', isim=isim)

# Yönlendirme örneği
@app.route('/anasayfa')
def anasayfa():
    return redirect(url_for('index'))  # /'ye yönlendirir
    # return redirect("https://google.com")

# Hata sayfası özelleştirme
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/iletisim', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        ad = request.form['ad']
        # Burada e-posta gönderme, veritabanına yazma vs. yapılabilir
        mesaj = f"Teşekkürler, {ad}! Mesajınız alındı."
        return render_template('contact.html', mesaj=mesaj)
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)