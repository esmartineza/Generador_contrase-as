from funciones.encriptar import comprobar_con
from funciones.encriptar import desencriptar_con
from funciones.encriptar import encriptar_con
def comprobar():
    while True:
        print('''
        1.Comprobar Contraseñas
        2.Encriptar Contraseñas
        3.Desencriptar Contraseñas
        4.Salir
        ''')
        opcion = int(input("ingrese opcion: "))
        if opcion == 1:
            comprobar_con()
        elif opcion == 2:
            encriptar_con()
        elif opcion == 3:
            desencriptar_con()
        else:
            print("Salio de comprobador de contraseñas")
            break
            