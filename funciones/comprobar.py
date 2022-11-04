def comprobar():
    print('''
    1.Comprobar Contraseñas
    2.Encriptar Contraseñas
    3.Desencriptar Contraseñas
    4.Salir
    ''')
    opcion = int(input("ingrese opcion: "))
    if opcion == 1:
        print("Comprobacion de contraseña ")
        contraseña = len(input("Ingrese Contraseña: "))
        #como primer punto para que la contraseña robusta debe contar con almenos 12 caracteres
        if contraseña < 8:
                print("su contraseña es vunerable es necesario cambiarla")
        else:
            print("contraseña segura")
    if opcion == 2:
        print("Encriptar Contraseña")
        contraseña = int(input("Ingrese Contraseña: "))
    else:
        print("Salio de comprobador de contraseñas")
        