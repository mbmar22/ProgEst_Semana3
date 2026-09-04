# Sumar 2 números
def sumar(numero1, numero2):
    return numero1 + numero2

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un número: "))

print(sumar(num1, num2))

sumar = sumar(15, 17)

print(sumar)

def restar(numero1 = 0, numero2 = 2):
    return (numero1 - numero2)

resta = restar(4, 2)
print(resta)

resta = restar(numero2 = 6, numero1 = 2)
print(resta)

resta = restar(8)
print(resta)

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    try:
        return numero1/ numero2
    except ZeroDivisionError:
        return "El segundo valor debe ser diferente que 0"

print(multiplicar(4, 2))

print(dividir(20, 5))

# Siempre crear variables en inglés.