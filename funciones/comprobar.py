from cryptography.fernet import Fernet

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
            print("Comprobacion de contraseña ")
            contraseña = len(input("Ingrese Contraseña: "))
            #como primer punto para que la contraseña robusta debe contar con almenos 12 caracteres
            if contraseña < 8:
                    print("su contraseña es vunerable es necesario cambiarla")
            else:
                print("contraseña segura")
        elif opcion == 2:
            print("Encriptar Contraseña")
            contraseña = input("Ingrese Contraseña: ")
            key = Fernet.generate_key()
            clave_cifrada = Fernet(key)
            clave_encriptada = clave_cifrada.encrypt(str.encode(contraseña))
            print(clave_encriptada)
        elif opcion == 3:
            print("Desencriptar Contraseña")
            contraseña = input("Ingrese Contraseña: ")
            desencriptado = clave_cifrada.decrypt(clave_encriptada)
            contraseña_desencriptada =  desencriptado.decode()
            print(contraseña_desencriptada)
        else:
            print("Salio de comprobador de contraseñas")
            