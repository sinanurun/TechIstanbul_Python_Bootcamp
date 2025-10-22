from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Geçici veri deposu (uygulama yeniden başlatılınca silinir)
kisiler = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ad = request.form.get('ad')
        email = request.form.get('email')
        if ad and email:
            kisiler.append({"ad": ad, "email": email})
        # POST’tan sonra her zaman yönlendir! (PRG pattern)
        return redirect('/')
    
    # GET → form + liste göster
    return render_template('index.html', kisiler=kisiler)

if __name__ == "__main__":
    app.run(debug=True)