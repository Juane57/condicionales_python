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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

#Ingresar la temperatura

num1 = float(input("Ingrese el primer valor de temperatura : "))

num2 = float(input("Ingrese el segundo valor de teperatura:  "))

num3 = float(input("Ingrese el tercer valor de temperatura:  "))

temp_a = 0
temp_b = 0
temp_p = (num1 + num2 + num3) / 3 

if num1 > num2 and num1 > num3:
    temp_a = num1
elif num2 > num1 and num2 > num3:
    temp_a = num2
else:
    temp_a = num3

if num1 < num2 and num1 < num3:
    temp_b = num1
elif num2 < num1 and num2 < num3:
    temp_b = num2
else:
    temp_b = num3


print(f"La temperara mas alta es {temp_a}º")
print(f"La temperatura mas baja es {temp_b}º")
print(f"La temperatura prromedio es {temp_p}º")


print("Fin del programa")