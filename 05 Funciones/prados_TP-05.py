from math import pi

##1. Crear una función llamada imprimir_hola_mundo que imprima por
##pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
##programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

##2. Crear una función llamada saludar_usuario(nombre) que reciba
##como parámetro un nombre y devuelva un saludo personalizado.
##Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
##volver: “Hola Marcos!”. Llamar a esta función desde el programa
##principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}! Que alegría volver a verte por acá :D")

nombre = input("¿Cómo te llamás? ")
saludar_usuario(nombre)


##3. Crear una función llamada informacion_personal(nombre, apellido,
##edad, residencia) que reciba cuatro parámetros e imprima: “Soy
##[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
##dir los datos al usuario y llamar a esta función con los valores in-
##gresados.


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
          
nombre = input("Como te llamás? ")
apellido = input("Cual es tu apellido? ")
edad = input("Cuantos años tenés? ")
residencia = input("En dónde vivís? ")

informacion_personal(nombre, apellido, edad, residencia)

##4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
##dio como parámetro y devuelva el área del círculo. calcular_peri-
##metro_circulo(radio) que reciba el radio como parámetro y devuel-
##va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
##bas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    print(pi*(radio**2), " cm cuadrados")

def calcular_perimetro_circulo(radio):
    print((2*pi)*radio, " cm")

radio = int(input("Ingrese el radio del círculo en cm por favor: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

##5. Crear una función llamada segundos_a_horas(segundos) que reciba
##una cantidad de segundos como parámetro y devuelva la cantidad
##de horas correspondientes. Solicitar al usuario los segundos y mos-
##trar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = segundos % 60
    print(f"{segundos} segundos son {horas} horas con {minutos} minutos")

segundos = int(input("Ingrese segundos para ver cuanto minutos son: "))
segundos_a_horas(segundos)

##6. Crear una función llamada tabla_multiplicar(numero) que reciba un
##número como parámetro y imprima la tabla de multiplicar de ese
##número del 1 al 10. Pedir al usuario el número y llamar a la fun-
##ción.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero*i)

numero=int(input("Ingrese un numero para que mostremos su tabla del 1 al 10: "))
tabla_multiplicar(numero)

##7. Crear una función llamada operaciones_basicas(a, b) que reciba
##dos números como parámetros y devuelva una tupla con el resulta-
##do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
##sultados de forma clara.

def operaciones_basicas(a, b):
    tuple=(a+b, a-b, a*b, a/b)
    print(f"El resultado de la suma es {tuple[0]}")
    print(f"El resultado de la resta es {tuple[1]}")
    print(f"El resultado de la multiplicacion es {tuple[2]}")
    print(f"El resultado de la division es {tuple[3]}")

a = float(input("Ingrese el primer número sobre el que ejecutar las operaciones: "))
b = float(input("Ingrese el segundo número sobre el que ejecutar las operaciones: "))

operaciones_basicas(a,b)

##8. Crear una función llamada calcular_imc(peso, altura) que reciba el
##peso en kilogramos y la altura en metros, y devuelva el índice de
##masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
##ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc= peso/(altura **2)
    print(f"Su IMC es {imc:.2f}")

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

calcular_imc(peso, altura)


