class futbolcu():
    kosu = "koşabilir"
    depar = "depar atar"
    maas = 500
    def __init__(self,ayak="sağ"):
        self.mevki = "orta"
        self.ayak = ayak
    pass
class basketbolcu():
    turnike = "turnike atabilir"
    ucluk = "üçlük atabilir"
    maas = 750
    def __init__(self):
        self.bolge = "ileri"
    pass
class multisporcu(basketbolcu,futbolcu):
    def __init__(self,ayak):
        basketbolcu.__init__(self)
        futbolcu.__init__(self,ayak)
    pass
mahmut = multisporcu("sol")
print(mahmut.turnike)
print(mahmut.kosu)
print(mahmut.maas)
print(mahmut.bolge)
print(mahmut.mevki)
print(mahmut.ayak)