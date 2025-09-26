dogum_yili = int(input("Doğum Yılınızı Giriniz : "))
yas = 2025 - dogum_yili
if yas >= 18:
    print("ehliyet alacak yaştasınız")
else:
    print("ehliyet almak için yaşınız tutmuyor")
    print(f"ehliyet alamazsınız, {yas} yaşında olduğunuz için")
    print(f"ehliyet almak için {18 - yas} yıl beklemelisin")

#yukarıdaki örnekte if else yapısı kullanıldı
#örnekte yaş 18 den büyük veya eşit ise if altındaki kod bloğu çalışır
#örnekte yaş 18 den küçük ise else altındaki kod bloğu çalışır