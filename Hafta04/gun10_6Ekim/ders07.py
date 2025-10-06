# oop de method çeşitleri

"""
| Tür               | Parametre | Erişebilir         | Çağrılma Yeri              | Amaç                             |
| ----------------- | --------- | ------------------ | -------------------------- | -------------------------------- |
| `instance method` | `self`    | Nesne değişkenleri | Nesne üzerinden            | Nesneye özgü işlemler            |
| `class method`    | `cls`     | Sınıf değişkenleri | Sınıf veya nesne üzerinden | Tüm sınıfı ilgilendiren işlemler |
| `static method`   | Yok       | Hiçbirine          | Sınıf veya nesne üzerinden | Yardımcı fonksiyonlar            |

"""

"""
1. Normal (Instance) Method

Bunlar, sınıftan oluşturulan nesneye (instance’a) ait metotlardır.
İlk parametre self olmalıdır. Bu, nesnenin kendisini temsil eder.
"""

class Ogrenci:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def bilgi_goster(self): #instance method
        print(f"Ad: {self.ad}, Yaş: {self.yas}")

# Nesne oluşturma
ogr1 = Ogrenci("Sinan", 20)
ogr1.bilgi_goster()  # ➜ Ad: Sinan, Yaş: 20

# __init__ bir constructor (yapıcı) metottur, nesne oluşturulurken otomatik çağrılır.

# bilgi_goster normal bir metottur; self üzerinden nesne verilerine erişir.


"""
2. Class Method (@classmethod)

Bu metotlar sınıfın kendisine aittir, nesneye değil.
İlk parametre olarak cls alır (class’ı temsil eder).
@classmethod dekoratörü ile tanımlanır.

"""

class Ogrenci:
    okul_adi = "Techİstanbul Akademi"

    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    @classmethod #classmethod başına eklenir
    def okul_bilgisi(cls): #parametre olarak cls alır ki bu sınıfı temsil eder
        print(f"Bu öğrenciler {cls.okul_adi} okuluna gidiyor.")

# Sınıftan direkt çağırılabilir
Ogrenci.okul_bilgisi()
# ➜ Bu öğrenciler Techİstanbul Akademi okuluna gidiyor.

# cls, sınıfın kendisini temsil eder.

# okul_adi gibi class değişkenlerine erişmek için kullanılır.

# Nesne oluşturmadan çağrılabilir.

"""
3. Static Method (@staticmethod)

Bu metotlar ne sınıfa ne de nesneye bağlıdır —
bağımsız fonksiyonlar gibidir ama sınıf içinde tanımlanır.
@staticmethod dekoratörü kullanılır ve ne self ne cls parametresi alır.
"""

class Matematik:
    @staticmethod
    def topla(a, b):
        return a + b

    @staticmethod
    def carp(a, b):
        return a * b

print(Matematik.topla(5, 3))  # ➜ 8
print(Matematik.carp(4, 2))   # ➜ 8

# Yardımcı (utility) işlemler için idealdir.

# self veya cls almaz, çünkü sınıfın durumuna erişmez.