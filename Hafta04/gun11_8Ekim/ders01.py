#@property Nedir?

# Sınıf içindeki bir metodu, özellik (attribute) gibi kullanmamızı sağlar.
# Yani parantez kullanmadan çağırabiliriz.
# Genellikle okuma, yazma ve silme kontrolü için kullanılır.

# class Dikdortgen:
#     def __init__(self, en, boy):
#         self.en = en
#         self.boy = boy

#     @property
#     def alan(self):
#         """Dikdörtgenin alanını döndürür"""
#         return self.en * self.boy

# dik = Dikdortgen(5, 3)
# print(dik.alan)  # parantez yok! ➜ 15


#@property ile değer atamak
# class Dikdortgen:
#     def __init__(self, en, boy):
#         self._en = en
#         self._boy = boy

#     @property
#     def en(self):
#         return self._en

#     @en.setter
#     def en(self, deger):
#         if deger > 0:
#             self._en = deger
#         else:
#             print("En pozitif olmalı!")

# dik = Dikdortgen(5, 3)
# print(dik.en)  # 5

# dik.en = 10
# print(dik.en)  # 10

# dik.en = -3    # En pozitif olmalı!
# print(dik.en)  # 10 (değişmedi)

# _en → private (gizli) değişken mantığı, setter/getter ile kontrol sağlanıyor

# class Dikdortgen:
#     def __init__(self, en, boy):
#         self._en = en
#         self._boy = boy

#     @property
#     def en(self):
#         return self._en

#     @en.deleter
#     def en(self):
#         print("En silindi!")
#         del self._en

# dik = Dikdortgen(5, 3)
# del dik.en  # En silindi!


"""
| Dekoratör    | Ne yapar                                   | Kullanım          |
| ------------ | ------------------------------------------ | ----------------- |
| `@property`  | Metodu **okuma için attribute gibi** yapar | `alan = dik.alan` |
| `@x.setter`  | Değer atamaya izin verir ve kontrol sağlar | `dik.en = 10`     |
| `@x.deleter` | Değişkeni siler                            | `del dik.en`      |


Önemli:  @property = getter
            @x.setter = setter
            @x.deleter = deleter

"""