##1) Dado el diccionario precios_frutas
##precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
##1450}

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

##2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
##desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


##3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
##desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
##precios.

print(precios_frutas.keys())

##4) Escribí un programa que permita almacenar y consultar números telefónicos.
##•Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
##•Luego, pedí un nombre y mostrale el número asociado, si existe.
'''
numerosTelefonicos={}

while len(numerosTelefonicos.keys()) < 5:
    nombre = input("Ingrese un nombre para agregar a la lista o fin para salir \n")
    if nombre.lower() == 'fin':
        break
    numero = input("Ingrese un numero para agregar a la lista o fin para salir \n")
    if numero.lower() == 'fin':
        break
    numerosTelefonicos[nombre]=numero

##print(numerosTelefonicos)
nombre = input("Ingrese un nombre para consultar su teléfono \n")

if nombre in numerosTelefonicos:
    print(numerosTelefonicos[nombre])
else:
    print("Ese nombre no está registrado")

##5) Solicita al usuario una frase e imprime:
##•Las palabras únicas (usando un set).
##•Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase \n")

palabras = frase.split()
palabrasUnicas = set(palabras)

frecuencia = {}

for i in palabras:
    if i in frecuencia:
        frecuencia[i] += 1
    else:
        frecuencia[i] = 1

print("Palabras únicas:", palabrasUnicas)
print("Frecuencia de cada palabra:", frecuencia)


##6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
##Luego, mostrá el promedio de cada alumno.

alumnos={}

while len(alumnos.keys()) < 3:
    nombre = input("Ingresa el nombre del alumno\n")
    notas = input("Ingresa tres notas\n")
    notasAlumno=tuple(notas.split())
    alumnos[nombre]=notasAlumno

for i in alumnos.keys():
    suma = int(alumnos[i][0])+int(alumnos[i][1])+int(alumnos[i][2])
    print(f"{i} tiene un promedio de "+str(suma/3))
'''
##7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
##•Mostrá los que aprobaron ambos parciales.
##•Mostrá los que aprobaron solo uno de los dos.
##•Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

alumnos={1:"Pedro", 2:"Esteban", 3:"Julio", 4:"Denise", 5:"José"}
listaAprobaronAmbos=[]
listaAprobaronUno=[]
listaAprobaronAlMenosUno=[]

aprobadosParcial1={1, 2, 3}
aprobadosParcial2={2, 3, 4}

aprobaronAmbos = aprobadosParcial1 & aprobadosParcial2
aprobaronUno = aprobadosParcial1 ^ aprobadosParcial2
aprobaronAlMenosUno = aprobadosParcial1 | aprobadosParcial2

for i in aprobaronAmbos:
    listaAprobaronAmbos.append(alumnos[i])

for i in aprobaronUno:
    listaAprobaronUno.append(alumnos[i])

for i in aprobaronAlMenosUno:
    listaAprobaronAlMenosUno.append(alumnos[i])

print(f"Aprobaron ambos parciales: {listaAprobaronAmbos}")
print(f"Aprobaron un solo parcial:  {listaAprobaronUno}")
print(f"Aprobaron al menos un parcial:  {listaAprobaronAlMenosUno}")
