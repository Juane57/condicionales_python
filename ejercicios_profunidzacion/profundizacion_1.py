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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

#Introducir numeros por consola

num1 = int(input("Ingrese su numero: "))

num2 = int(input("Ingrese su numero: "))

resul = num1 - num2

if resul > 0:
    print(" El resultado es Positivo")
elif resul < 0:
    print(" El resultado es Negativo")
else:
    print("El resultado es 0")

print("Fin del programa")