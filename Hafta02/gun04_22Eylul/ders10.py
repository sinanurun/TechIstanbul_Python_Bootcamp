kume1 = {"a","b","c",2}
kume2 = {1,2,3}

# kume3 = kume1.union(kume2)
kume3 = kume1 | kume2
print(kume1,kume2,kume3)

kume4 = {"8",9,45}
# kume3 = kume4 | kume2 | kume1
kume3 = kume4.union(kume2,kume1)
print(kume3)
demet = (7,8,6,45,9)
kume3 = kume4.union(demet)
print(kume3)

# kume4.update(demet)
# print(kume4)

kume3 = kume4.intersection(demet)
kume3 = kume4 & set(demet)
print(kume3)