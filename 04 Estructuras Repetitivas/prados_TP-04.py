from random import randrange
from statistics import mean

##1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
##(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


##2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
##dígitos que contiene.

numero = input("Ingrese un numero para que contemos la cantidad de digitos que contiene \n")
cantidad = 0

for i in numero:
    cantidad +=1
    print(i)

print(cantidad)

##3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
##dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese el primer numero \n"))
num2 = int(input("Ingrese el segundo numero \n"))
contador = 0

for i in range(num1+1,num2):
    contador += i

print(contador)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
acumulador = 0

while True:
    num = int(input("Ingrese un numero para sumar o 0 para salir \n"))
    acumulador += num
    if num == 0:
        break

print(acumulador)


##5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
##programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
numero = randrange(0,10)
contador = 0

while True:
    num = int(input("Ingrese un numero entre 0 y 9 \n"))
    contador += 1

    if num == numero:
        print(f"Adivinaste! El número era el: {numero}. Te tomaron {contador} intentos")
        break
    else:
        num = ("Lo siento no adivinaste.\n")

##6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
##entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)


##7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
##número entero positivo indicado por el usuario.
num2 = int(input("Ingrese un numero, vamos a sumar todos los hasta ese numero \n"))
contador = 0

for i in range(1,num2):
    contador += i

print(contador)

##8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
##programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
##negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
##menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares=0
impares=0
positivos=0
negativos=0
cero=0
contador=0

for i in range(100):
    num = int(input("Ingrese un numero, vamos a ver si es par, impar, positivo o negativo \n"))
    if num == 0:
        cero += 1
    else:
        if num % 2 == 0:
            pares +=1
            if num > 0:
                positivos += 1
            elif num < 0:
                negativos +=1
        elif num % 2 != 0:
            impares +=1
            if num > 0:
                positivos += 1
            elif num < 0:
                negativos +=1

print(f"Ingresaste {cero} ceros, {impares} numeros impares, {pares} numeros pares y entre ellos {negativos} eran negativos y {positivos} eran positivos")

##9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
##media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
##poder procesar 100 números cambiando solo un valor).
contador=0
acumulador=0

for i in range(100):
    acumulador += int(input("Ingrese un número \n"))
    contador +=1

print("Media aritmética: ", acumulador/contador)

##10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
##usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
acumulador = input("Ingrese un número para invertir \n")

print("El numero invertido es: ")
for i in range(len(acumulador), 0, -1):
    print(acumulador[i-1], end="")
print("")