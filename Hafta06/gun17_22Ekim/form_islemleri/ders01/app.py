from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ad = request.form.get('ad')  # .get() → None döner (hata vermez)
        if ad:
            return f"<h1>Merhaba, {ad}!</h1><a href='/'>Geri dön</a>"
        else:
            return "<h2>Hata: Ad boş olamaz!</h2><a href='/'>Tekrar dene</a>"
    # GET isteği → formu göster
    return '''
    <h2>Adını Gir</h2>
    <form method="POST">
        <input type="text" name="ad" placeholder="Adınız" required>
        <button type="submit">Gönder</button>
    </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)