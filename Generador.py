
from funciones.comprobar import comprobar
from funciones.letras import letras
print("Detector y Generador de Contraseñas")

while True:
    
    print('''Seleccione una opcion 
    1.Comprobar si la contraseña es segura 
    2.Generar contraseñas
    3.Salir
    ''')
    opcion =input("ingrese opcion: ")
    if opcion == "1":
        comprobar()
    elif opcion == "2":
        letras()
    else:
        print("El generador fue apagado")
        break

