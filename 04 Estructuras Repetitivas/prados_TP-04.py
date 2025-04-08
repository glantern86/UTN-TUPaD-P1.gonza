'''
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
'''

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


