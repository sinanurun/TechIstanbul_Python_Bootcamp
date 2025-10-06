# ÖRNEK 3: Çeşitli Metod Türleri
class BankaHesabi:
    """Banka hesabı sınıfı"""
    
    def __init__(self, hesap_sahibi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye
        self.islem_gecmisi = []
    
    def para_yatir(self, miktar):
        """Hesaba para yatırır"""
        if miktar > 0:
            self.bakiye += miktar
            self.islem_gecmisi.append(f"+{miktar} TL yatırıldı")
            return f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL"
        else:
            return "Geçersiz miktar!"
    
    def para_cek(self, miktar):
        """Hesaptan para çeker"""
        if miktar > 0 and miktar <= self.bakiye:
            self.bakiye -= miktar
            self.islem_gecmisi.append(f"-{miktar} TL çekildi")
            return f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL"
        else:
            return "Geçersiz işlem!"
    
    def bakiye_sorgula(self):
        """Mevcut bakiyeyi gösterir"""
        return f"Güncel bakiye: {self.bakiye} TL"
    
    def hesap_ozeti(self):
        """Hesap özetini gösterir"""
        ozet = f"Hesap Sahibi: {self.hesap_sahibi}\n"
        ozet += f"Bakiye: {self.bakiye} TL\n"
        ozet += "İşlem Geçmişi:\n"
        for islem in self.islem_gecmisi[-5:]:  # Son 5 işlem
            ozet += f"  - {islem}\n"
        return ozet

# Kullanım
hesap = BankaHesabi("Ahmet Yılmaz", 1000)
print(hesap.bakiye_sorgula())
print(hesap.para_yatir(500))
print(hesap.para_cek(200))
print(hesap.hesap_ozeti())