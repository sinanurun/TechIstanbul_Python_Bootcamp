from flask import Flask, render_template

app = Flask(__name__)

# Geçici todo listesi (gerçek projede veritabanı olur)
todos = [
    {"id": 1, "gorev": "Flask öğren", "tamamlandi": True},
    {"id": 2, "gorev": "Jinja2 çalış", "tamamlandi": False},
    {"id": 3, "gorev": "Sanal ortam kur", "tamamlandi": False},
    {"id": 4, "gorev": "Todo listesi yap", "tamamlandi": True}
]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)