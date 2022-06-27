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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

texto_1 = str(input("Ingrese su primera palabra: "))
texto_2 = str(input("Ingrese su segunda palabra: "))
texto_3 = str(input("Ingrese su tercera palabra: "))



result_1 = texto_1, texto_2, texto_3
restul_2 = texto_1, texto_3, texto_2
restul_3 = texto_2, texto_1, texto_3
restul_4 = texto_2, texto_3, texto_1
result_5 = texto_3, texto_1, texto_2
result_6 = texto_3, texto_2, texto_1

alf = int(input("Ingrese el Nº 1 pra ordenar las palabras por orden alfabetico: \nIngrese el Nº 2 para ordenar las palabras por su cantidad de letras:\n"))

if alf == 1:
    if texto_1 > texto_2 and texto_1 > texto_3:
        if texto_2 > texto_3:
            print(result_1)
        else:
            print(restul_2)
    elif texto_2 > texto_1 and texto_2 > texto_3:
        if texto_1 > texto_3:
            print (restul_3)
        else:
            print(restul_4)
    elif texto_3 > texto_1 and texto_3 > texto_2:
        if texto_1 > texto_2:
            print(result_5)
        else:
            print (result_6)
elif alf ==2:
    if len(texto_1) > len(texto_2) and len(texto_1) > len(texto_3):
        if len(texto_2) > len(texto_3):
            print(result_1)
        else:
            print(restul_2)
    elif len(texto_2) > len(texto_1) and len(texto_2) > len(texto_3):
        if len(texto_1) > len(texto_3):
            print (restul_3)
        else:
            print(restul_4)
    elif len(texto_3) > len(texto_1) and len(texto_3) > len(texto_2):
        if len(texto_1) > len(texto_2):
            print(result_5)
        else:
            print (result_6)

print("Fin del programa")