# ÖRNEK 5: Private Özellikler
class SifreYoneticisi:
    """Şifre yönetimi sınıfı"""
    
    def __init__(self, kullanici_adi):
        self.kullanici_adi = kullanici_adi
        self.__sifre = ""  # Private özellik (__ ile başlar)
        self.__sifre_olusturuldu = False
    
    def sifre_ayarla(self, yeni_sifre):
        """Şifre ayarlama metodu"""
        if len(yeni_sifre) >= 6:
            self.__sifre = yeni_sifre
            self.__sifre_olusturuldu = True
            return "Şifre başarıyla ayarlandı"
        else:
            return "Şifre en az 6 karakter olmalıdır"
    
    def sifre_kontrol(self, girilen_sifre):
        """Şifre kontrol metodu"""
        if not self.__sifre_olusturuldu:
            return "Henüz şifre ayarlanmamış"
        
        if girilen_sifre == self.__sifre:
            return "Şifre doğru"
        else:
            return "Şifre yanlış"
    
    def sifre_gucu(self):
        """Şifre gücünü kontrol eder (private metod)"""
        if not self.__sifre:
            return "Şifre ayarlanmamış"
        
        uzunluk_puani = min(len(self.__sifre) // 2, 5)  # Maksimum 5 puan
        return f"Şifre gücü: {uzunluk_puani}/5"

# Kullanım
sifre_yoneticisi = SifreYoneticisi("ahmet123")
print(sifre_yoneticisi.sifre_ayarla("gizli123"))
print(sifre_yoneticisi.sifre_kontrol("gizli123"))
print(sifre_yoneticisi.sifre_gucu())

# Private özelliğe doğrudan erişim (hata verir)
# print(sifre_yoneticisi.__sifre)  # Hata!