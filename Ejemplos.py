from cryptography.fernet import Fernet
# antes de utilizar es necesario instalar lo siguiente pip install cryptography



while True:
    print('''
    1.encriptar 
    2.desencriptar 
    3.salir
    ''')
    opcion = input("ingrese la opcion: ")
    if opcion == "1":
        texto = input("ingrese contraseña: ")
        key = Fernet.generate_key()
        clave_cifrada = Fernet(key)
        clava_encriptada = clave_cifrada.encrypt(str.encode(texto))
        print(clava_encriptada)
    elif opcion == "2":
        texto = input("ingrese la contraseña encriptada: ")
        desencriptado = clave_cifrada.decrypt(clava_encriptada)
        texto_desencriptado = desencriptado.decode()
        print(texto_desencriptado)

    else:
        print("apagado")
        break