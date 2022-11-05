import random

def gen_letras():
    try:
        seleccion = int(input("ingrese la cantidad de caracteres  deseados: "))
        minusculas ="abcdefghijklmnopqrstuvwxyz"
        mayusculas = minusculas.upper()        
        conc_letras = minusculas + mayusculas
        gen_letras = random.sample(conc_letras, seleccion)
        pass_letras = "".join(gen_letras)
        print(pass_letras)
    except:
        print('''
        -----------------------------------------------
        |sobrepasaste la cantidad maxima de caracteres|
        -----------------------------------------------
        ''')