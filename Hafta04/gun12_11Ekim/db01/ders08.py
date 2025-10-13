# kitaplık uygulaması fonksiyonel
import sqlite3
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
veritabanim = bulundugum_dizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabanim)



def listele_kitaplari():
    baglanti = sqlite3.connect(veritabanim)
    imlec = baglanti.cursor()

    # Tüm kitapları oku
    imlec.execute("SELECT * FROM kitaplar")

    # Tek bir sonuç almak için: imlec.fetchone()
    # Tüm sonuçları almak için: imlec.fetchall() liste döndürür
    kitaplar = imlec.fetchall()

    for kitap in kitaplar:
        print(f"ID: {kitap[0]}, Ad: {kitap[1]}, Yazar: {kitap[2]}")
    
    if len(kitaplar)>0:
        return True
    else:
        print("Listelenecek Kitap Bulunamadı")
        return False

def ekle_kitap():
    ad = input("Kitap Adı: ")
    yazar = input("Yazar Adı: ")
    
    # baglanti = sqlite3.connect('kutuphane.db')
    baglanti = sqlite3.connect(veritabanim)
    imlec = baglanti.cursor()
    
    imlec.execute("INSERT INTO kitaplar VALUES (NULL, ?, ?)", (ad, yazar))
    
    baglanti.commit()
    baglanti.close()
    print(f"'{ad}' başarıyla eklendi.")

def guncelle_kitap():
    
    liste_bilgisi = listele_kitaplari()
    if liste_bilgisi:

        kitap_id = int(input("Güncellemek istediğiniz kitabın id bilgisini giriniz"))
        yeni_ad = input("Güncellemek istediğiniz kitabın yeni ad bilgisini giriniz")
        imlec = baglanti.cursor()
        imlec.execute("UPDATE kitaplar SET ad = ? WHERE id = ?", (yeni_ad, kitap_id))
        
        baglanti.commit()
        baglanti.close()
        print(f"ID {kitap_id} olan kitabın adı '{yeni_ad}' olarak güncellendi.")
    else:
        print("Liste boş olduğu için güncelleme işlemi yapılamıyor")

def sil_kitap():
        
    liste_bilgisi = listele_kitaplari()
    if liste_bilgisi:

        kitap_id = int(input("Silmek istediğiniz kitabın id bilgisini giriniz"))
        imlec = baglanti.cursor()   
        imlec.execute("DELETE FROM kitaplar WHERE id = ?", (kitap_id,)) 
        baglanti.commit()
        baglanti.close()
        print(f"ID {kitap_id} olan kitap veritabanından silindi.")
    else:
        print("Liste boş olduğu için silme işlemi yapılamıyor")

def en_cok_kitap_yazari():

    imlec = baglanti.cursor()
    # Yazar ismine göre grupla ve her grubun satır sayısını say (COUNT)
    imlec.execute("SELECT yazar, COUNT(id) FROM kitaplar GROUP BY yazar ORDER BY COUNT(id) DESC LIMIT 1")
    sonuc = imlec.fetchone()
    baglanti.close()
    if sonuc:
        print(f"\nEn çok kitaba sahip yazar: {sonuc[0]} ({sonuc[1]} kitap)")
    else:
        print("Veritabanında kitap yok.")

yeni_kitaplar = [
    ("1984", "George Orwell"),
    ("Hayvan Çiftliği", "George Orwell"),
    ("Suç ve Ceza", "Dostoyevski")
]

def coklu_kitap_ekle(kitap_listesi):
    imlec = baglanti.cursor()
    
    for ad, yazar in kitap_listesi:
        imlec.execute("INSERT INTO kitaplar VALUES (NULL, ?, ?)", (ad, yazar))
    
    baglanti.commit()
    baglanti.close()
    print(f"{len(kitap_listesi)} adet kitap eklendi.")

# coklu_kitap_ekle(yeni_kitaplar)

def kitap_ara(kelime):
    imlec = baglanti.cursor()
    
    # % işareti, kelimenin önünde veya arkasında herhangi bir şey olabilir anlamına gelir.
    imlec.execute("SELECT ad, yazar FROM kitaplar WHERE ad LIKE ?", (f'%{kelime}%',))
    kitaplar = imlec.fetchall()
    
    baglanti.close()
    
    if kitaplar:
        print(f"\n'{kelime}' içeren kitaplar:")
        for ad, yazar in kitaplar:
            print(f"- {ad} (Yazar: {yazar})")
    else:
        print(f"'{kelime}' içeren kitap bulunamadı.")

# kitap_ara("Sefil")
def karsilama():

    while True:
        print("yapmak istediğiniz işlemi seçiniz")
        islemler = """1 - kitapları listele
        2- kitap ekle
        3- kitap guncelle
        4- kitap sil
        5- çıkış
        """
        islem = int(input(islemler))
        match islem:
            case 1:
                listele_kitaplari()
            case 2 :
                ekle_kitap()
            case 3 :
                guncelle_kitap()
            case 4 :
                sil_kitap()
            case 5:
                break
            case _:
                print("Hatalı işlem girişi yapıldı")

if __name__ == "__main__":
    karsilama()