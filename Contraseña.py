import random
import string

print("Detector y Generador de Contraseñas")

print('''Seleccione una opcion 
1.comprobar si la contraseña es segura 
2.generar contraseñas
''')
opcion =input("ingrese opcion: ")
while True:
    if opcion == "1":
        print("Comprobacion de contraseña ")
        contraseña = len(input("Ingrese Contraseña: "))
        #como primer punto para que la contraseña robusta debe contar con almenos 12 caracteres
        if contraseña <= 8:
            print("su contraseña es vunerable es necesario cambiarla")
        else:
            print("contraseña segura")
    if opcion == "2":
        print("Generar contraseña aleatoria")
        seleccion = int(input("ingrese la cantidad de caracteres  deseados: "))
        if seleccion >= 8:
            minusculas ="abcdefghijklmnopqrstuvwxyz"
            generacion = random.sample(minusculas, seleccion)
            password = "".join(generacion)
            print(password )
        else:
            print("la contraseña tiene que tener como minimo 8 caracteres")


