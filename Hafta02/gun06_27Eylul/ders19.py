# recursive fonksiyon örneği
def faktoriyel_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel_recursive(n - 1)
# Kullanım
for i in range(6):
    print(f"{i}! = {faktoriyel_recursive(i)}")