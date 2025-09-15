"""1’den 100’e kadar sayıları yazdır:

3’e bölünen → "Fizz"
5’e bölünen → "Buzz"
İkisine de bölünen → "FizzBuzz"
Hiçbiri değilse → sayıyı yaz
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)