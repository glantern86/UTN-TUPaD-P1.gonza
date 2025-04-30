'''
##1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
##range.

multiplos = list(range(4, 101, 4))
print(multiplos)


##2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
##penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
##indexing con números negativos!
listaList = [ "papitas", 23, [ "mago", "vampiro", "hombre lobo" ]]

print(listaList[2][-2])


##3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
##pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por

voidList = []
voidList.append("tomate, lechuga, remolacha")
print(voidList)

##4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
##respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
##en los videos o bien investigar cómo funciona el indexing con números negativos!

animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[-1]="oso"

print(animales)


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

##Lo que hace el código es utilizar la funcion remove sobre la lista 'numeros'. A la 
## funcion remove en los parámetros le pasaron la funcion max con la lista como parametro.
## Asi que la funcion max obtiene el numero maximo de la lista, se lo pasa al remove y este 
## saca el numero más elevado de la lista.


##6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
##pantalla los dos primeros.

listaNum = list(range(10, 30, 5))
print(listaNum[:2])

##7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
##cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1]="pollo"
autos[2]="duran duran"

print(autos)
'''



