# Condicionales [Python]
# Ejercicios de práctica

# Autor: Juan Emilio Dalcol
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print(f"El strig '{texto_1}' es mayor alfabeticamente al strig '{texto_2}'")
else:
    print (f"El strig '{texto_2}' es mayor alfabeticamente al strig '{texto_1}'")

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
num1 = int(texto_1)
num2 = int(texto_2)

if num1 > num2:
    print(f"El numero {num1} es mayor al numero {num2}")
elif num2 > num1:
     print(f"El numero {num2} es mayor al numero {num1}")
else:
    print("Los numeros son iguales")

print("Fin del programa")
# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
# porque el numero Siete comienza con S y el Cinco con C.


