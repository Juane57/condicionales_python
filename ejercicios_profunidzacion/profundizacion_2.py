# Condicionales [Python]
# Ejercicios de profundización

# Autor: Juan Emilio Dalcol
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

# Ingresar los numero por consola

num1 = int(input("Ingrese su primer numero: "))

num2 = int(input("Ingrese su segundo numero: "))

num3 = int(input("Ingrese su tercer numero:  "))

if (num1 % 2) == 0:
    print(f"El numero '{num1}' es par")
else:
    print(f"El numero '{num1}' es impar")

if (num2 % 2) == 0:
    print(f"El numero '{num2}' es par")
else:
    print(f"El numero '{num2}' es impar")

if (num3 % 2) == 0:
    print(f"El numero '{num3}' es par")
else:
    print(f"El numero '{num3}' es impar")

print("Fin del programa")