yol = float(input("kaç km yol gittiniz"))
zaman = float(input("kaç saat zaman gittiniz"))
hiz = yol / zaman


if hiz > 132:
    print(f"hız sınırınız aştınız hızınız {hiz}")
    print(f"hız sınırını {hiz - 120} km/h kadar aştınız")
    print(f"hız sınırını aştığınız için {(hiz - 120)*50} tl trafik cezası aldınız")

else:
    print("kurallara uyduğunuz için tebrikler \n iyi sürüşler dileriz")