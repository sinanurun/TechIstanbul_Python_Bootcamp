sayilar = [1,2,3,4,5,6]
kareler = {str(x)*2 : x**2 for x in sayilar }
print(kareler)

kelimeler = ["oguzhan","onur"]
harf_sayili = {kelime: "" for kelime in kelimeler}
print(harf_sayili)