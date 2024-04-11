# ACTIVIDAD 1 CADENAS
# Crea una nueva cadena con el siguiente contenido: "Python es un lenguaje de programación versátil"

cadena_1 = "versátil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"

cadena_final = cadena_2 + " " + cadena_3 + " " + cadena_4 + " " + cadena_1
print(cadena_final)


# ACTIVIDAD 2 NUMEROS
# Descripción de la actividad.

"""En nuestro trabajo, nos solicitan desarrollar un programa que permita calcular el promedio final de los equipos de futbol en un torneo. 
Para ello, debemos considerar tres aspectos: 
Jugaron 20 partidos durante el torneo.
Los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntosEl promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos"""

partidos_jugados = 20
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = partidos_jugados - partidos_ganados - partidos_empatados

puntos_totales = (
    (partidos_ganados * 3) + (partidos_empatados * 1) + (partidos_perdidos * 0)
)
promedio_final = puntos_totales / partidos_jugados

print("El promedio final de los equipos en el torneo es:", promedio_final)


# Desafío Slicing
cadena = "acitametaM ,5.8 ,otipeP ordeP"

# Dar vuelta la cadena
cadena_volteada = cadena[::-1]

# Extraer nombre y apellido
nombre_alumno = cadena_volteada.split(",")[0].strip()

print(cadena_volteada)
print(nombre_alumno)

# 3. Extraer la nota y almacenarla en una variable llamada nota.
nota = float(cadena_volteada.split(",")[1].strip())

# 4. Extraer la materia y almacenarla en una variable llamada materia.
materia = cadena_volteada.split(",")[2].strip()

# 5. Mostrar por pantalla la siguiente estructura, usando la concatenación de cadenas:
print(nombre_alumno, "ha sacado un", nota, "en", materia)

# Mi primer programa en Python

nota_1 = float(input("Ingrese la nota 1: "))  # Ingresamos la nota 1
nota_2 = float(input("Ingrese la nota 2: "))  # Ingresamos la nota 2
nota_3 = float(input("Ingrese la nota 3: "))  # Ingresamos la nota 3

nota_final = (
    (nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3 * 0.5)
)  # Calculamos la nota final

print("La nota final es:", nota_final)  # Mostramos la nota final
