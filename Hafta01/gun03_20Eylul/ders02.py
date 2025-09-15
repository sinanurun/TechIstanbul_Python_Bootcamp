ad = input("adınızı giriniz")
yas = int(input("yaşınızı giriniz"))
for dd in range(yas):
    print("{}. {}".format(dd+1,ad))

for ks in range(len(ad)):
    print("{}. {} {}".format(ks+1, ad, ad[ks]))