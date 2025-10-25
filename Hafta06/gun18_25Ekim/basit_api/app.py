from flask import Flask, jsonify, request
import json
import os

# Flask uygulamasını başlat
app = Flask(__name__)

# JSON dosya yolu
USERS_FILE = 'users.json'

# --- Yardımcı Fonksiyonlar ---

def load_users():
    """JSON dosyasından kullanıcı verilerini okur. Dosya yoksa veya boşsa boş liste döner."""
    if not os.path.exists(USERS_FILE) or os.path.getsize(USERS_FILE) == 0:
        return []
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            # Dosya boşsa veya geçersiz JSON içeriyorsa (JSONDecodeError) yakalanır
            return json.load(f)
    except json.JSONDecodeError:
        # JSON bozuksa hata mesajı verip boş liste ile devam et
        print(f"UYARI: {USERS_FILE} dosyası bozuk veya geçersiz JSON içeriyor. Boş liste ile devam ediliyor.")
        return []

def save_users(users):
    """Kullanıcı verilerini JSON dosyasına yazar."""
    # ensure_ascii=False: Türkçe karakterlerin (ç, ş, ğ, vs.) JSON'da düzgün görünmesini sağlar.
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def initialize_users_file():
    """Uygulama ilk kez çalıştırıldığında users.json dosyasını örnek verilerle oluşturur."""
    if not os.path.exists(USERS_FILE) or os.path.getsize(USERS_FILE) == 0:
        # Kullanıcının sağladığı örnek veriyi varsayılan olarak ayarlıyoruz.
        initial_users = [
            {"id": 1, "name": "Ahmet Yılmaz", "email": "ahmet@example.com"},
            {"id": 2, "name": "Ayşe Demir", "email": "ayse@example.com"}
        ]
        save_users(initial_users)
        print(f"Bilgi: {USERS_FILE} dosyası örnek verilerle oluşturuldu.")

# --- API Uç Noktaları (Routes) ---

# Ana sayfa
@app.route('/', methods=['GET'])
def home():
    """API'nin genel durumunu ve mevcut uç noktalarını listeler."""
    return jsonify({
        "message": "Flask REST API çalışıyor! Kullanıcı yönetimi için endpoints:",
        "endpoints": {
            "GET /users": "Tüm kullanıcıları listeler",
            "GET /users/<id>": "Belirli bir kullanıcıyı getirir",
            "POST /users": "Yeni kullanıcı oluşturur (Gerekli: name, email)",
            "PUT /users/<id>": "Kullanıcıyı günceller (Opsiyonel: name, email)",
            "DELETE /users/<id>": "Kullanıcıyı siler"
        }
    })

# 1. Tüm kullanıcıları listele
@app.route('/users', methods=['GET'])
def get_users():
    """Tüm kullanıcıları listeler."""
    users = load_users()
    # Hata ayıklama için: Eğer boş liste dönüyorsa konsola bilgi yazdır
    if not users:
        print("HATA AYIKLAMA BİLGİSİ: '/users' endpoint'i boş liste döndü. 'users.json' dosyasının doğru yerde, dolu ve geçerli JSON formatında olduğundan emin olun.")
    return jsonify(users), 200

# 2. Belirli bir kullanıcıyı getir
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Belirli bir ID'ye sahip kullanıcıyı getirir."""
    users = load_users()
    # next() ile tek satırda kullanıcıyı bulma, bulunamazsa None döner
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user:
        return jsonify(user), 200
    else:
        # Kullanıcı bulunamazsa 404 Not Found
        return jsonify({"error": f"ID {user_id} ile kullanıcı bulunamadı"}), 404

# 3. Yeni kullanıcı ekle
@app.route('/users', methods=['POST'])
def create_user():
    """Yeni bir kullanıcı oluşturur."""
    # silent=True, isteğin JSON formatında olmaması durumunda hatayı sessizce yutarak None dönmesini sağlar.
    data = request.get_json(silent=True) 

    if not data:
        return jsonify({"error": "Geçerli bir JSON verisi gereklidir"}), 400
        
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "İsim ('name') ve e-posta ('email') alanları zorunludur"}), 400

    users = load_users()
    
    # ID oluşturma: Mevcut en büyük ID'yi bul ve 1 artır. 
    # default=0 ile boş liste durumunda 1'den başlar.
    new_id = max([u.get('id', 0) for u in users], default=0) + 1
    
    new_user = {
        "id": new_id,
        "name": name,
        "email": email
    }
    users.append(new_user)
    save_users(users)
    
    # 201 Created status kodu ile yeni oluşturulan kullanıcıyı döndür
    return jsonify(new_user), 201

# 4. Kullanıcıyı güncelle
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Belirli bir ID'ye sahip kullanıcıyı günceller."""
    users = load_users()
    # next() ve enumerate() ile kullanıcının indeksini bulma
    user_index = next((i for i, u in enumerate(users) if u['id'] == user_id), None)

    if user_index is None:
        return jsonify({"error": f"ID {user_id} ile kullanıcı bulunamadı"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Güncellenecek veri içeren geçerli bir JSON gereklidir"}), 400

    updated = False
    
    # Sadece gönderilen alanları güncelle
    if 'name' in data and data['name']: # Boş string gönderilmesini de engelle
        users[user_index]['name'] = data['name']
        updated = True
    if 'email' in data and data['email']: 
        users[user_index]['email'] = data['email']
        updated = True

    if updated:
        save_users(users)
        return jsonify(users[user_index]), 200
    else:
        # Geçerli güncelleme verisi yoksa 400 Bad Request döndür
        return jsonify({"error": "Güncellenecek geçerli bir alan (name veya email) bulunamadı"}), 400


# 5. Kullanıcıyı sil
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Belirli bir ID'ye sahip kullanıcıyı siler."""
    users = load_users()
    # next() ve enumerate() ile kullanıcının indeksini bulma
    user_index = next((i for i, u in enumerate(users) if u['id'] == user_id), None)

    if user_index is None:
        return jsonify({"error": f"ID {user_id} ile kullanıcı bulunamadı"}), 404

    # pop() ile kullanıcıyı listeden sil
    deleted_user = users.pop(user_index)
    save_users(users)
    
    # 200 OK status kodu ile başarılı mesajı döndür
    return jsonify({
        "message": f"Kullanıcı ID {user_id} ({deleted_user['name']}) başarıyla silindi"
    }), 200

# Uygulamayı başlat
if __name__ == '__main__':
    # Başlangıçta users.json dosyasını kontrol et ve gerekirse örnek veriyle oluştur.
    initialize_users_file() 
    app.run(debug=True, host='0.0.0.0', port=5000)
