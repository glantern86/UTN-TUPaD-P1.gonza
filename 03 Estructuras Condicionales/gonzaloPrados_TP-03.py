import random
from statistics import mode,median, mean

'''
##1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
##deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad por favor \n"))

if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

##2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
##mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
##mensaje “Desaprobado”.

nota = int(input("Ingrese su nota por favor \n"))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

##3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
##número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
##contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
##operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero por favor \n"))

if numero%2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

##4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
##siguientes categorías pertenece:
##●​ Niño/a: menor de 12 años.
##●​ Adolescente: mayor o igual que 12 años y menor que 18 años.
##●​ Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
##●​ Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad por favor \n"))

if edad < 12:
    print("Usted es un Niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es un Adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un Adulto/a joven")
elif edad >= 30:
    print("Usted es un Adulto")

##5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
##(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
##pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
##pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
##de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
##como una lista o un string.

password = input("Ingrese una contraseña de entre 8 y 14 caracteres \n")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


##6)Escribir un programa que tome la lista
##numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
##hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios, "\n")
print("Media aritmética: ", mean(numeros_aleatorios))
print("Moda única: ",mode(numeros_aleatorios))
print("Mediana: ",median(numeros_aleatorios))

##7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
##termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
##pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
##pantalla.
frase = input("Ingrese una frase por favor \n")

if frase[-1] == ('a' or 'e' or 'i' or 'o' or 'u'):
    print(frase + "!")
else:
    print(frase)

##8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
##dependiendo de la opción que desee:
##1.​ Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
##2.​ Si quiere su nombre en minúsculas. Por ejemplo: pedro.
##3.​ Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
##El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
##usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
##lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre por favor \n")
funcion = int(input("Seleccione una opcion \n"
"1.​ Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n"
"2.​ Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n"
"3.​ Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n"))

if funcion == 1:
    print(nombre.upper())
elif funcion == 2:
    print(nombre.lower())
elif funcion == 3:
    print(nombre.title())

##9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
##magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
##por pantalla:
##●​ Menor que 3: "Muy leve" (imperceptible).
##●​ Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
##●​ Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
##generalmente no causa daños).
##●​ Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
##débiles).
##●​ Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
##●​ Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto por favor \n"))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
'''
##10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
##del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
##si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese (N)orte o (S)ur de acuerdo al hemisferio en el que te encuentras")
mes = int(input("Ingrese un numero del 1-12 para el mes actual"))
dia = int(input("Ingrese el dia actual"))

if mes == 12 OR mes <= 3:
    if mes == 12 AND dia > 21:
    
    elif mes == 3 AND dia < 20:

##arreglar este asco





