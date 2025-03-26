#Pedimos nombre y edad por consola
edad = int(input("Cual es tu edad?: "))
nombre = input("Cual es tu nombre?: ")

#Si edad es mayor a 18 y si nombre es tato, ponemos hola mundo, si el nombre no es tato ponemos Chau
if edad > 18:
  if nombre == "Tato":
    print("Hola Mundo!")
  else:
      print("Chau")
else:
    print("No sos mayo de edad")

