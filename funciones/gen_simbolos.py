import random

def gen_simbolos():
    try:
        seleccion = int(input("ingrese la cantidad de caracteres  deseados: "))
        simbolos="@()[]{}*,;/-_¿?.¡!$<#>&+%="
        gen_simbolos = random.sample(simbolos, seleccion)
        pass_simbolos = "".join(gen_simbolos)
        print(pass_simbolos)    
    except:
        print('''
            -----------------------------------------------
            |sobrepasaste la cantidad maxima de caracteres|
            -----------------------------------------------
            ''')