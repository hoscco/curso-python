# Definición de la función
def evaluar_numero(numero):
    if numero == 10:
        print("El número ingresado es 10")
    elif numero == 7:
        print("Se ha ingresado un comodín")
    elif numero % 2 == 0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")

# Función principal
def main():
    numero = int(input("Ingrese un número: "))
    evaluar_numero(numero)

# Llamada a la función principal
if __name__ == "__main__":
    main()