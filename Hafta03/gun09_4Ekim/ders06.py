#dosya silme işlemleri
import os

bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))

os.remove(bulundugum_dizin+"/myfile.txt")


if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

