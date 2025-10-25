from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "site.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Uygulama bağlamında veritabanını oluştur
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Kullanıcı adı zaten alınmış.')
            return redirect(url_for('register'))
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Kayıt başarılı! Giriş yapabilirsiniz.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Giriş başarılı!')
            return redirect(url_for('dashboard'))
        else:
            flash('Geçersiz kullanıcı adı veya şifre.')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', username=user.username)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Çıkış yaptınız.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)