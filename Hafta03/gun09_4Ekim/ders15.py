import os

with open("txt_dosyalari.txt", "w") as f:
    for dosya in os.listdir("."):
        if dosya.endswith(".txt"):
            f.write(dosya + "\n")

