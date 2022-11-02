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
