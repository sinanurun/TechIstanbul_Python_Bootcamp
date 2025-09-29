import turtle

print("=== TURTLE İLE ÇİZİM ===")

ok = turtle.Turtle()
ok.forward(100)
ok.right(90)
ok.forward(100)
ok.right(90)
ok.forward(100) 
ok.right(90)
ok.forward(100)



ekran = turtle.Screen()
ekran.bgcolor("lightblue")    


ok.forward(150)
ok.right(120)
ok.forward(150)
ok.right(120)
ok.forward(150)
ok.right(120)

ekran.exitonclick()  # Tıklamayı bekler

#ok.done() # Çizimi bitir
