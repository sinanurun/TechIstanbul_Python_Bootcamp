from functools import reduce
# reduce fonksiyonunu programımıza dahile delim

# bir listenin en büyük elemanını bulalım
# f = lambda a,b: a if (a > b) else b
# sonuc = reduce(f, [8,9,45,2,65,89,5,6,78])
# print(sonuc)
# print(reduce(f, [8,9,45,2,65,89,5,6,78]))

# faktoriyel hesaplayalım

fhesap = lambda x,y: x*y
# print(reduce(fhesap,[1,2,3,4,5,6,7,8,9]))
# print(reduce(fhesap,[x for x in range(1,10)]))

# sonuc2 = reduce(lambda x, y: x*y, range(44,49))/reduce(lambda x, y: x*y, range(1,7))
# print(sonuc2)