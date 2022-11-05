import random

def gen_random():
    try:
        seleccion = int(input("ingrese la cantidad de caracteres  deseados: "))
        minusculas ="abcdefghijklmnopqrstuvwxyz"
        mayusculas = minusculas.upper()
        numero ="0123456789"
        simbolos="@()[]{}*,;/-_¿?.¡!$<#>&+%="
        conc = minusculas + mayusculas + numero + simbolos
        generacion = random.sample(conc, seleccion)
        password = "".join(generacion)
        print(password)
    except:
        print('''
            -----------------------------------------------
            |sobrepasaste la cantidad maxima de caracteres|
            -----------------------------------------------
            ''')