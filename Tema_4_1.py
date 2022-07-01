# Escribe un programa que pregunte al usuario su edad
# y muestre por pantalla si es mayor de edad o no.

edad = int(input("Por favor, introduzca su edad: "))

if edad < 18:
    print("No eres mayor de edad")
else:
    print("Eres mayor de edad")