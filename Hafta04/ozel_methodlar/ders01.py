#normal bir fonksiyonun yazılışı
"""
def kare(x):
    # y = x**2
    return x**2 #y
print(kare(2))
"""
# lambda ile yukarıdaki fonksiyonun yazılışı

k = lambda x: x**2
print(k)
print(k(2))


bk = lambda x,y: x if x>y else y
print(bk(5,8))

"""
def bk(x,y):
    if x>y:
        return x
    else:
        return y
print(bk(5,8))
"""