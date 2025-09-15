notunuz = int(input("Sınav notunuz: "))

if notunuz >= 90:
    harf = "AA"
elif notunuz >= 80:
    harf = "BA"
elif notunuz >= 70:
    harf = "BB"
elif notunuz >= 60:
    harf = "CB"
elif notunuz >= 50:
    harf = "CC"
else:
    harf = "FF"

print("Harf notunuz:", harf)