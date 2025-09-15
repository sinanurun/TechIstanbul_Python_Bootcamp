demet = (24,8, 2.5, True,"Mert",["Mert","Seçme","CEng"],(24,8,2.5,True,"Mert",[""]))
print(demet)
print(type(demet))
pazar = ["elma","armut","salatalık","marul"]
pazarDemeti = tuple(pazar)
print(pazarDemeti)
print(demet.index("Mert"))
print(demet.count("Mert"))
for eleman in demet:
    print(eleman)

dlist = list(demet)
dlist[1] = "mahmut"
demet = tuple(dlist)
print(demet)

print(pazarDemeti[0])
print(pazarDemeti[-1])
print(pazarDemeti[::-1])