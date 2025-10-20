from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello(): #hello(): Bu route’a gelen isteklerde çalışacak fonksiyon.
    return "Merhaba Flask Tech İstanbul"


@app.route('/selam/<isim>')
def selam(isim):
    bugun = datetime.now().strftime("%d.%m.%Y")
    return render_template('index.html', isim=isim, tarih=bugun)


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True): Geliştirme sunucusunu başlatır; debug=True sayesinde kodda değişiklik yapınca otomatik yeniden yüklenir.