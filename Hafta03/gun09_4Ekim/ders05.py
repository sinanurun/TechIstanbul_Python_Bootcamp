import os

bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
#dosya oluşturma
f = open(bulundugum_dizin+"/myfile.txt", "x", encoding="utf-8")