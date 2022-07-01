# Escribe un programa capaz de mostrar todos los números impares
# desde un número de inicio y otro final. Por ejemplo: teniendo
# numero_inicial = 2 y numero_final = 8, el programa debe
# imprimir por consola: [3, 5, 7]

numeroInicial = int(input("Por favor, introduzca el número inicial: "))
numeroFinal = int(input("Ahora introduzca el número final: "))
numeros = []

for n in range(numeroInicial, (numeroFinal + 1)):
    if n % 2 == 1:
        numeros.append(n)

print(numeros)