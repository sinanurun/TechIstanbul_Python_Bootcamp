adet = int(input("kaç dilim pizza istersiniz"))
dilim = adet
a = 1
while adet > 0:
    print(a,". pizzanız afiyet olsun")
    adet = adet - 1
    a += 1

print("---"*5)
i = 1
while i <= dilim:
    print(i,".pizzanız afiyet olsun")
    i +=1
