from cryptography.fernet import Fernet

def comprobar_con():
    print("Comprobacion de contraseña ")
    contraseña = len(input("Ingrese Contraseña: "))
    #como primer punto para que la contraseña robusta debe contar con almenos 12 caracteres
    if contraseña < 8:
        print("su contraseña es vunerable es necesario cambiarla")
    else:
        print("contraseña segura")   
def encriptar_con():
    print("Encriptar Contraseña")
    contraseña = input("Ingrese Contraseña: ")
    key = Fernet.generate_key()
    clave_cifrada = Fernet(key)
    clave_encriptada = clave_cifrada.encrypt(str.encode(contraseña))
    print(clave_encriptada)    
    
def desencriptar_con():
    print("Desencriptar Contraseña")
    contraseña = input("Ingrese Contraseña: ")
    desencriptado = contraseña.decrypt(contraseña)
    contraseña_desencriptada = desencriptado.decode()
    print(contraseña_desencriptada)    