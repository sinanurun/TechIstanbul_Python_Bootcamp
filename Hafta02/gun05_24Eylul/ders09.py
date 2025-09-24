oyuncular = {
    "bjk": ["rafa","cengiz","salih"],
    "fb" : ["talisca","asensio","fred"],
    "gs" : ["oshimen","sane","icardi"]
}

print(oyuncular["bjk"])
print(oyuncular["fb"])
print(oyuncular["gs"])

for takim in oyuncular:
    print(takim)
   # print(oyuncular[takim])
    for oyuncu in oyuncular[takim]:
        print("\t",oyuncu)