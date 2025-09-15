"""
Bir fırın ısınıyor. 50°C, 100°C, 150°C gibi adımlarla ısınıyor. 
Ama 100°C’de “Dikkat: Orta sıcaklık” uyarısı veriliyor ama 
işlem devam ediyor. 
200°C’ye ulaşınca “Hazır!” deniyor.
"""
sicaklik = 0

while sicaklik <= 200:
    sicaklik = sicaklik + 50
    if sicaklik == 100:
        print(" Dikkat: Orta sıcaklık!")
        continue  # uyarıyı ver, ama devam et
    print(f"Fırın {sicaklik}°C")