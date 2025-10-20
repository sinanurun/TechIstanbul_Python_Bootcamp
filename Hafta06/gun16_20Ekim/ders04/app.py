from flask import Flask

app = Flask(__name__)
#Flask(__name__): Flask uygulama nesnesini oluşturur.

#@app.route('/'): Ana sayfayı (/) tanımlar.
@app.route("/")
def hello(): #hello(): Bu route’a gelen isteklerde çalışacak fonksiyon.
    return "Merhaba Flask Tech İstanbul"


@app.route("/hakkimizda")
def hakkimizda():
    return "Hakkımızda sayfasına hoşgeldiniz"

@app.route('/yil/<int:yil>')
def yil_goster(yil):
    return f"Seçilen yıl: {yil}"

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True): Geliştirme sunucusunu başlatır; debug=True sayesinde kodda değişiklik yapınca otomatik yeniden yüklenir.