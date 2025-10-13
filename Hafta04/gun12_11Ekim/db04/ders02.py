# Kullanıcıdan isim, telefon, email al, SQLite veritabanında sakla.
import sqlite3

def baglanti_olustur():
    baglanti = sqlite3.connect("rehber.db")
    cursor = baglanti.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kisiler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            telefon TEXT UNIQUE,
            email TEXT
        )
    ''')
    baglanti.commit()
    return baglanti, cursor

def kisi_ekle(cursor, baglanti):
    isim = input("İsim: ")
    telefon = input("Telefon: ")
    email = input("Email: ")
    
    try:
        cursor.execute('''
            INSERT INTO kisiler (isim, telefon, email)
            VALUES (?, ?, ?)
        ''', (isim, telefon, email))
        baglanti.commit()
        print(f"{isim} rehbere eklendi.")
    except sqlite3.IntegrityError:
        print("Hata: Bu telefon numarası zaten kullanılıyor.")

def kisileri_listele(cursor):
    cursor.execute("SELECT * FROM kisiler")
    kayitlar = cursor.fetchall()
    for k in kayitlar:
        print(f"{k[0]}. {k[1]} | {k[2]} | {k[3]}")

# Ana menü
baglanti, cursor = baglanti_olustur()

while True:
    print("\n=== REHBER ===")
    print("1. Kişi Ekle")
    print("2. Tüm Kişileri Listele")
    print("3. Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        kisi_ekle(cursor, baglanti)
    elif secim == "2":
        kisileri_listele(cursor)
    elif secim == "3":
        baglanti.close()
        print("Rehber kapatılıyor.")
        break