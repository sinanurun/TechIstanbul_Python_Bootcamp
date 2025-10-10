class Futbolcu():
    kosu = "koşabilir"
    depar = "depar atar"
    maas = 500
    def __init__(self,ayak="sağ"):
        self.mevki = "orta"
        self.ayak = ayak
    pass
class Basketbolcu():
    turnike = "turnike atabilir"
    ucluk = "üçlük atabilir"
    maas = 750
    def __init__(self):
        self.bolge = "ileri"
    pass
class MultiSporcu(Basketbolcu,Futbolcu):
    def __init__(self,ayak):
        Basketbolcu.__init__(self)
        Futbolcu.__init__(self,ayak)
    pass
mahmut = MultiSporcu("sol")
print(mahmut.turnike)
print(mahmut.kosu)
print(mahmut.maas)
print(mahmut.bolge)
print(mahmut.mevki)
print(mahmut.ayak)