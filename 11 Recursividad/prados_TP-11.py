##1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
##función para calcular y mostrar en pantalla el factorial de todos los números enteros
##entre 1 y el número que indique el usuario

def calcularFactorial(numero):
    if numero == 0:
        return 1
    else:
        return numero*calcularFactorial(numero-1)
    
def imprimirEnteros(numero):
    for i in range(1, numero+1):
        print(calcularFactorial(i))

imprimirEnteros(int(input("Ingresa un número: ")))

##2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
##indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
##especifique.

def calcularFibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return calcularFibonacci(posicion-1)+calcularFibonacci(posicion-2)
    
for i in range(10):
    print(calcularFibonacci(i))

##3) Crea una función recursiva que calcule la potencia de un número base elevado a un
##exponente, utilizando la fórmula 𝑛𝑚 = 𝑛∗𝑛(𝑚−1). Prueba esta función en un
##algoritmo general.


def calcularPotencia(numero, potencia):
    if potencia == 0:
        return 1
    else:
        return numero*calcularPotencia(numero, potencia-1)
    
print(calcularPotencia(5, 3))

##4) Crear una función recursiva en Python que reciba un número entero positivo en base
##decimal y devuelva su representación en binario como una cadena de texto.

def calcularBinario(numero):
    if numero <= 1:
        return numero
    else:
        return str(calcularBinario(numero//2)) + str(numero%2)
    
print(calcularBinario(8))

##5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
##cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
##lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

print(es_palindromo("mamam"))

##6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
##número entero positivo y devuelva la suma de todos sus dígitos

def suma_digitos(n):
    if n<=0:
        return n
    else:
        return suma_digitos(n//10) + n%10

print(suma_digitos(5107))

##7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
##bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
##último nivel con un solo bloque.
##Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
##nivel más bajo y devuelva el total de bloques que necesita para construir toda la
##pirámide.

def contar_bloques(n):
    if n ==1:
        return 1
    else:
        return n+contar_bloques(n-1)
    
print(contar_bloques(12))

##8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
##número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
##aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


print(contar_digito(98798799, 9))