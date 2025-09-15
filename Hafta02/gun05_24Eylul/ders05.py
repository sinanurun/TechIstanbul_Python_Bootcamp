treng = {"araba":"car","kalem":"pencil","kırmızı":"red"}
print(treng)
print(treng["araba"])

print(treng.values())
print(treng.keys())
print(treng.items())

for dd in treng:
    print(dd, treng[dd])

for key, value in treng.items():
    print(key, "=>", value)

for key, value in zip(treng.keys(), treng.values()):
    print(key, "==", value)
