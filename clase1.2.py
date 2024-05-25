def saludar():
    global nombre, apellido
    print("ingrese su nombre: ")
    nombre=input()
    print("ingrese su apellido: ")
    apellido=input()
    print(f"hola {nombre} {apellido}")

def calcular():
    global prom
    nota1=int(input("ingrese la nota 1: "))
    nota2=int(input("ingrese la nota 2: "))
    nota3=int(input("ingrese la nota 3: "))
    prom=(nota1+nota2+nota3)/3
    print(f"el promedio es {prom}")

def despedir():
    print(f"hasta luego {nombre} {apellido}")
    if prom > 15:
        print("aprobaste, felicidades!")
    else:
        print("reprobaste, sigue estudiando")

#cuerpo principal
saludar()
calcular()
despedir()