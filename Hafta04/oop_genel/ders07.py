class Sporcu():
    def __init__(self,ad,brans,altin,gumus,bronz):
        self.ad = ad
        self.brans = brans
        self.mbronz = bronz #public veri halka açık değişken
        self._mgumus = gumus #protected yarı gizli
        self.__maltin = altin #private tam gizli
    def atlet_bilgisi(self):
        return "Sporcu adı : {}, Branşı :{}".format(atlet1.ad,atlet1.brans)
    @property
    def a_yazdir(self):
        amadalya = self.__maltin
        return "altın madalya sayısı {}".format(self.__maltin)

atlet1 = Sporcu("ali","100 Metre",2,3,9)
print(atlet1.atlet_bilgisi())
print("bronz madalya sayısı",atlet1.mbronz)
print("gümüş madalya sayısı",atlet1._mgumus)
print(atlet1.a_yazdir)
