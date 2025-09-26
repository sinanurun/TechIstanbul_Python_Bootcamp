# Fibonacci serisi hesaplama
# Kullanıcıdan kaç terim istediğini alır ve Fibonacci serisini döner

def fibonacci(adet):
    seri = []
    a, b = 0, 1
    for _ in range(adet):
        seri.append(a)
        a, b = b, a + b
    return seri

# Kullanım
print("İlk 10 Fibonacci sayısı:", fibonacci(10))