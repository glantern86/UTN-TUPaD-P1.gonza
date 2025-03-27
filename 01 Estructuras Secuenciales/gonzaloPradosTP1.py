##1##
print("Hola Mundo")

##2##
print("Hola como te llamas?")
nombre = input()
print("Hola", nombre, "un gusto conocerte")

##3##
nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Por favor ingresa tu apellido: ")
lugarResidencia = input("Por favor indica tu lugar de residencia: ")
print("Tu Nombre es {nombre} tu apellido es {apellido} y tu lugar actual de residencia es {lugarResidencia}")


##4##
import math
print("Ingresa el radio de un circulo")
radio = int(input())
area= math.pi*(radio ** 2)
perimetro = math.pi*2*radio
print(f"El area de circulo es {area} y su perimetro es {perimetro}")


##5##
print("Ingresa la cantidad de segundos que deseas convertir a horas")
segundos = float(input())
horas= segundos/7200
print(f"La cantidad de horas es {horas}")


##6##
print("Ingrese un numero para obtener su tabla hasta el 9")
numero = int(input())
i = 1
for i in range (1, 10):
    print(f"{numero} x {i} = {numero*i}")

##7##
print("Ingrese un numero entero distinto de cero")
numero1 = int(input())
print("Ingrese otro numero entero distinto de cero")
numero2 = int(input())

print(f"La suma de {numero1} y {numero2} es: ", numero1+numero2 )
print(f"La resta de {numero1} y {numero2} es: ", numero1-numero2 )
print(f"La multiplicacion de {numero1} y {numero2} es: ", numero1*numero2 )
print(f"La division de {numero1} y {numero2} es: ", numero1/numero2 )

##8##
print("Ingrese su altura en metros")
altura = float(input())
print("Ingrese su peso en kilos")
peso = float(input())
print("Su indice de masa corporal es: ", peso/(altura**2))

##9##
print("Ingrese una temperatura en grados celsius")
temperatura = float(input())
print("La temperatura en grados Fahrenheit es: ", (9/5)*temperatura+32)

##10##
print("Ingresa 3 numeros")
num1 = float(input())
num2 = float(input())
num3 = float(input())
print("El promedio de los tres numeros es: ", (num1+num2+num3)/3)

print("Git es complicado de aprender pero vale la pena")