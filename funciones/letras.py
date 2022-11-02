import random

def letras():
    print("Generar contraseña aleatoria")
    seleccion = int(input("ingrese la cantidad de caracteres  deseados: "))
    print('''Seleccione una opcion 
        1.solo letras(Max 54)
        2.solo numeros(Max 10)
        3.Solo Simbolos(Max 26)  
        4.Contraseña aleatoria(Max 88)
        5.Salir
        ''')  
    opciones = int(input("Seleccione una de las opciones: "))
    minusculas ="abcdefghijklmnopqrstuvwxyz"
    mayusculas = minusculas.upper()
    numero ="0123456789"
    simbolos="@()[]{}*,;/-_¿?.¡!$<#>&+%="

    if opciones == 1:
        conc_letras = minusculas + mayusculas
        gen_letras = random.sample(conc_letras, seleccion)
        pass_letras = "".join(gen_letras)
        print(pass_letras)
    elif opciones == 2:
        gen_numeros = random.sample(numero, seleccion)
        pass_numeros = "".join(gen_numeros)
        print(pass_numeros)
    elif opciones == 3:   
        gen_simbolos = random.sample(simbolos, seleccion)
        pass_simbolos = "".join(gen_simbolos)
        print(pass_simbolos)
    elif opciones == 4:
        conc = minusculas + mayusculas + numero + simbolos
        generacion = random.sample(conc, seleccion)
        password = "".join(generacion)
        print(password)
    else:
        print("salir")