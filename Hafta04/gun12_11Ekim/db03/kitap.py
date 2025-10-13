class Kitap:
    """
    Veritabanındaki bir kitap kaydını (satırını) temsil eder.
    Bu, bir ORM'deki 'Model' kavramına benzer.
    """
    def __init__(self, ad, yazar, id=None):
        # id=None varsayılan değeri, kitap henüz veritabanına kaydedilmediğinde
        # ID'sinin olmadığını belirtir. Veritabanı bunu otomatik olarak verecektir.
        self.id = id
        self.ad = ad
        self.yazar = yazar
    
    # __str__ ve __repr__ metotları (4. Hafta 2. Oturum konusu) 
    # nesneyi yazdırırken anlaşılır çıktı vermemizi sağlar.
    def __str__(self): #kullanıcı için
        return f"Kitap ID: {self.id if self.id else 'Yeni'}, Ad: {self.ad}, Yazar: {self.yazar}"

    def __repr__(self): #geliştirici için
        return f"Kitap(id={self.id}, ad='{self.ad}', yazar='{self.yazar}')"