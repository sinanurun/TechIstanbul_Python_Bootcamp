"""
Python OOP: Erişim Belirteçleri (Access Modifiers)
Giriş: Neden Erişim Kontrolü Gerekir? (Kapsülleme)
Nesne Yönelimli Programlama (OOP), veriyi (nitelikler/değişkenler) ve bu veri üzerinde çalışan işlevleri (metotlar) bir araya getirerek (Sınıf dediğimiz yapıları) programlamayı düzenler.

Erişim Belirteçleri ise bir sınıfın içindeki bazı bilgilerin veya işlevlerin, sınıfın dışından doğrudan değiştirilip değiştirilemeyeceğini, yani gizli kalıp kalmayacağını belirler.

Buna Kapsülleme (Encapsulation) denir. Amacı şudur:

Güvenlik: Kritik verilerin yanlışlıkla veya kasten bozulmasını önlemek. (Örnek: Banka hesabının bakiyesini dışarıdan direkt değiştirememek.)

Düzen: Sınıfın iç işleyişini dış dünyadan gizlemek ve kodun bakımını kolaylaştırmak.
"""

"""
Geleneksel OOP dillerinin aksine, Python'da aslında "Private" (Özel) veya "Protected" (Korumalı) anahtar kelimeleri yoktur.

Python, bunun yerine "Geliştiricilere Güven" felsefesini benimser ve bu erişim seviyelerini adlandırma kurallarıyla (konvansiyonlarla) belirtir. Bu konvansiyonlar şunlardır:

Erişim Seviyesi	Tanımlama Şekli	Konvansiyon Adı	Gerçek Erişim Durumu
Halka Açık	Normal İsim (isim)	Public	Her yerden erişilebilir.
Yarı Özel	Tek Alt Çizgi (_isim)	Protected	Her yerden erişilebilir, ama "Lütfen dışarıdan dokunmayın" mesajı verir.
Özel	Çift Alt Çizgi (__isim)	Private	Sınıf dışından erişimi zorlaştırır (Name Mangling).
"""

"""
1. Public (Halka Açık) Üyeler
Tanımlama: Normal bir isimle başlar (önünde alt çizgi yok).
Erişim: Sınıfın içinden, dışından, alt sınıflardan, her yerden direkt erişilebilir.

Kullanım Amacı: Sınıfınızın dış dünyaya sunduğu resmi arayüzdür. Kullanıcıların güvenle kullanması beklenen metot ve niteliklerdir.

Örnek: Public Üye
"""

class Araba:
    def __init__(self, marka, renk):
        # Public Nitelikler (Herkesin görmesi ve değiştirmesi normal)
        self.marka = marka
        self.renk = renk

    def calistir(self):
        # Public Metot
        return f"{self.marka} çalıştırıldı."

# Sınıf dışından erişim
araba_obj = Araba("Volvo", "Kırmızı")

# Niteliklere doğrudan erişim ve değiştirme
print(f"Marka: {araba_obj.marka}")  # Çıktı: Marka: Volvo
araba_obj.renk = "Mavi" # Dışarıdan direkt değiştirdik
print(f"Yeni Renk: {araba_obj.renk}")  # Çıktı: Yeni Renk: Mavi

# Metoda erişim
print(araba_obj.calistir()) # Çıktı: Volvo çalıştırıldı.


"""
2. Protected (Korumalı) Konvansiyon
Tanımlama: Tek bir alt çizgi (_) ile başlar. (Örn: self._bakiye)
Erişim: Teknik olarak hala her yerden erişilebilir, ancak bu bir uyarı işaretidir.

Kullanım Amacı: Bu üyenin sınıfın iç işleyişine ait olduğunu, alt sınıflar tarafından kullanılmak üzere tasarlandığını, ancak dışarıdan doğrudan değiştirilmemesi gerektiğini belirtir.

Önemli Not: Python erişimi engellemez. Geliştirici olarak bu kurala uymak sizin sorumluluğunuzdadır.

Örnek: Protected Konvansiyon
Bir banka hesabında, bakiye (miktarı) sadece yatir() veya cek() gibi metotlarla değişmeli, dışarıdan direkt değiştirilmemelidir.

"""

class BankaHesabi:
    def __init__(self, hesap_no, bakiye=0):
        self.hesap_no = hesap_no  # Public
        # Protected Konvansiyon: Lütfen dışarıdan dokunma!
        self._bakiye = bakiye

    def yatir(self, miktar):
        self._bakiye += miktar
        print(f"Yeni Bakiye: {self._bakiye}")

    def _log_islemi(self, islem):
        # Protected Metot: Sadece sınıf içindeki diğer metotlar kullanmalı
        print(f"[LOG] İşlem Yapıldı: {islem}")

# Sınıf dışından erişim
hesap = BankaHesabi("12345", 1000)

# 1. Doğru Kullanım (Public metot ile bakiye değişimi)
hesap.yatir(500)
# Çıktı: Yeni Bakiye: 1500

# 2. Teknik Olarak Mümkün Olan, Ama Yanlış Kullanım (Kuralı İhlal)
# Python sizi engellemez, ama bu kötü bir programlama pratiğidir!
hesap._bakiye = 999999999  # Bakiye direkt bozuldu!

print(f"Hileli Bakiye: {hesap._bakiye}")


"""
3. Private (Özel) Üyeler
Tanımlama: Çift alt çizgi (__) ile başlar. (Örn: self.__parola)
Erişim: Bu, Python'da erişimi en çok kısıtlayan yöntemdir. Sınıfın dışından doğrudan erişilemez.

Kullanım Amacı: Sınıfın en kritik, en özel verilerini veya yardımcı metotlarını dış dünyadan gizlemek için kullanılır.

Nasıl Çalışır? (Name Mangling)
Python, çift alt çizgi ile başlayan bir nitelik veya metot gördüğünde, ismini otomatik olarak değiştirir. Bu işleme Name Mangling (İsim Karmaştırma) denir.

__gizli_veri → _SınıfAdı__gizli_veri olur.

Bu, dışarıdan doğrudan erişimi engeller ve bir AttributeError hatası almanıza neden olur.

Örnek: Private Üye
"""

class Kullanici:
    def __init__(self, isim, parola):
        self.isim = isim       # Public
        self.__parola = parola # Private

    def __parola_kontrol(self):
        # Private Metot
        return len(self.__parola) > 8

    def giris_yap(self, girilen_parola):
        if self.__parola_kontrol() and girilen_parola == self.__parola:
            return "Giriş başarılı!"
        else:
            return "Parola yanlış veya geçersiz."

# Sınıf dışından erişim
kullanici = Kullanici("Ali", "gizliparola123")

# 1. Public Niteliklere Erişim
print(kullanici.isim) # Çıktı: Ali

# 2. Private Nitelik/Metoda Doğrudan Erişim (HATA VERECEK)
try:
    print(kullanici.__parola) 
except AttributeError as e:
    print(f"\n[HATA] Doğrudan Erişim Engellendi: {e}")
    # Çıktı: [HATA] Doğrudan Erişim Engellendi: 'Kullanici' object has no attribute '__parola'

# 3. Public Metot Üzerinden Erişim (Doğru Kullanım)
print(kullanici.giris_yap("yanlisparola"))
# Çıktı: Parola yanlış veya geçersiz.
print(kullanici.giris_yap("gizliparola123"))
# Çıktı: Giriş başarılı!

# 4. Name Mangling (Zorla Erişim - Yapılmamalıdır!)
print(f"\nName Mangling ile erişim (YASAK!): {kullanici._Kullanici__parola}")
# Çıktı: Name Mangling ile erişim (YASAK!): gizliparola123


"""
Kural	    İsimlendirme	    Erişim Kısıtlaması	Amaç
Public	    degisken	        Hiçbir kısıtlama yok.	Sınıfın genel arayüzü.
Protected	_degisken	        Konvansiyonel uyarı. Teknik olarak erişim serbest.	Alt sınıflar için veya iç işleyiş için. Lütfen dokunma.
Private	    __degisken	        Name Mangling ile doğrudan erişim zorlaştırılır.	Kritik verileri ve iç yardımcı metotları gizlemek.
"""