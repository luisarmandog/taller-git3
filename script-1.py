#hello git 

import math

# suma 
def suma(a, b):
    return a + b

# Resta
def resta(a,b):
    return a - b

# multiplicacion
def multiplicacion(a,b):
    return a * b

# factorización 

def factorizacion(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

# division 

def division(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"

# Solicitar input al usuario
dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el divisor: "))

# Calcular la división y mostrar el resultado
resultado = division(dividendo, divisor)
print("Resultado:", resultado)


# iteración 

inicio = 1
fin = 10

for numero in range(inicio, fin+1):
    print(numero)

