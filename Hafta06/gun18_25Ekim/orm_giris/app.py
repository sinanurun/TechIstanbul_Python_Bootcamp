from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os  # <<<<<<< os modülünü içe aktarıyoruz

# Flask uygulamasını oluştur
app = Flask(__name__)

# Veritabanı dosya yolunu belirle
# Uygulamanın bulunduğu dizini (os.path.abspath(os.path.dirname(__file__))) kullanır
# ve bu dizine 'todo.db' adında bir dosya oluşturur.
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy nesnesini oluştur
db = SQLAlchemy(app)
# ORM Modeli: Todo
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.id}: {self.title}>'

# Uygulama bağlamı içinde veritabanı ve tabloları oluştur
with app.app_context():
    db.create_all()

# Ana sayfa rotası: Tüm görevleri listeler (R - Read)
@app.route('/')
def index():
    # Tüm todo öğelerini veritabanından çek
    todo_list = db.session.execute(db.select(Todo).order_by(Todo.id)).scalars().all()
    return render_template('index.html', todo_list=todo_list)

# Yeni görev ekleme rotası (C - Create)
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        new_todo = Todo(title=title, complete=False)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

# Görev durumunu güncelleme rotası (U - Update)
@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))

# Görev silme rotası (D - Delete)
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

# Uygulamayı çalıştır
if __name__ == '__main__':
    # Not: production ortamında debug=True kullanılmamalıdır.
    app.run(debug=True)