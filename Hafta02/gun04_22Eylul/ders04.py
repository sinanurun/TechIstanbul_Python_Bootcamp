meyve = ["elma", "ananas","çilek", "yabanmersini","ejder meyvesi"]
print(meyve)
meyve.append("çilek")
print(meyve)
print(meyve.count("çilek"))
print(meyve.index("yabanmersini"))
meyve.insert(2,"muz")
print(meyve)
meyve[2] = "mandalina"
print(meyve)
meyve.sort()
print(meyve)
meyve.reverse()
print(meyve)
yeni_meyveler = ["kivi", "portakal"]
meyve.extend(yeni_meyveler)
print(meyve)
yeni_meyveler2 = ["altın çilek", "böğürtlen"]
meyve.append(yeni_meyveler2)
print(meyve)
meyve.pop()
print(meyve)
meyve.pop(1)
print(meyve)
meyve.remove("ejder meyvesi")
print(meyve)
del meyve[1]
print(meyve)
meyve.clear()
print(meyve)
del meyve
print(meyve)