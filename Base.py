#prueba

def suma():
    x = int(input("Digite un número: \n"))
    y = int(input("Digite otro número: \n"))
    print("La suma",x,"+",y ,"es", x+y)

def resta():
    x = int(input("Digite un número: \n"))
    y = int(input("Digite otro número: \n"))
    print("La resta", x, "-", y, "es", x - y)

def menu():
    print("1 suma / 2 resta")
    opc = int(input("elija uan opcion: "))
    if opc == 1:
        suma()
    elif opc == 2:
        resta()
menu()
print("Hola Perros")

if menu() == 1:
    print("tengo hambre alv")

#esto es solo un archivo de pruebas
#hgxhgvjhg,jhg,jhgv,kjbkjbhlkjbk