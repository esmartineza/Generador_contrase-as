def comprobar():
        print("Comprobacion de contraseña ")
        contraseña = len(input("Ingrese Contraseña: "))
        #como primer punto para que la contraseña robusta debe contar con almenos 12 caracteres
        if contraseña < 8:
            print("su contraseña es vunerable es necesario cambiarla")
        else:
            print("contraseña segura")