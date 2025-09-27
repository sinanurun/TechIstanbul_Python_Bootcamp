# MODÜLLER - ÖRNEK 4
# Turtle Modülü - Grafik Çizimler

import turtle

print("=== TURTLE İLE ÇİZİM ===")

try:
    # Turtle ekranını ayarla
    ekran = turtle.Screen()
    ekran.bgcolor("lightblue")
    ekran.title("Python Turtle Çizimleri")
    
    # Turtle nesnesi oluştur
    t = turtle.Turtle()
    t.speed(3)  # Çizim hızı (1-10 arası)
    
    print("1: Kare Çiz")
    print("2: Daire Çiz") 
    print("3: Üçgen Çiz")
    print("4: Spiral Çiz")
    
    secim = int(input("Hangi şekli çizmek istersiniz? "))
    
    if secim == 1:
        # Kare çizimi
        t.color("red")
        for i in range(4):
            t.forward(100)  # 100 birim ileri
            t.right(90)     # 90 derece sağa dön
            
    elif secim == 2:
        # Daire çizimi
        t.color("green")
        t.circle(50)  # 50 birim yarıçaplı daire
        
    elif secim == 3:
        # Üçgen çizimi
        t.color("blue")
        for i in range(3):
            t.forward(100)
            t.left(120)  # 120 derece sola dön
            
    elif secim == 4:
        # Spiral çizimi
        t.color("purple")
        for i in range(36):  # 36 kere dönecek
            t.forward(i * 5)  # Her seferinde daha uzun çizgi
            t.right(30)       # 30 derece sağa dön
            
    else:
        print("Geçersiz seçim!")
    
    # Çizimi bitir
    t.hideturtle()  # Turtle'ı gizle
    print("Çizim tamamlandı! Pencereyi kapatmak için tıklayın.")
    ekran.exitonclick()  # Tıklamayı bekler
    
except ValueError:
    print("HATA: Lütfen geçerli bir sayı girin!")
except Exception as e:
    print(f"Beklenmeyen hata: {e}")

print("Turtle çizimleri bitti.")
