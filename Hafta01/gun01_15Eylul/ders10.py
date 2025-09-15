#mantıksal operatörler mantıksal verilerle işlem yapmak için kullanılır
#mantıksal operatörler işlem sonuçları da mantıksal olur
#and, or, not
# and operatörü iki ifadenin de doğru olması durumunda True döner
# or operatörü iki ifadeden birinin doğru olması durumunda True döner
# not operatörü ifadenin tersini döner True ise False, False ise True




print((55 == 45) and (8>4))
print((55 == 45) or (8>4))
print(not(55 == 88))

# öncelik sırası not -> and -> or
print((5>4) and (3==3) or (8<5) and not(4!=4) or (7==7))
print((5>4) and (3==3) or ((8<5) and (not(4!=4))) or (7==7))

