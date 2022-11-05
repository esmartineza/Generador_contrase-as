import random

def gen_numeros():
    try:
        seleccion = int(input("ingrese la cantidad de caracteres  deseados: "))
        numero ="0123456789"
        gen_numeros = random.sample(numero, seleccion)
        pass_numeros = "".join(gen_numeros)
        print(pass_numeros)
    except:
        print('''
        -----------------------------------------------
        |sobrepasaste la cantidad maxima de caracteres|
        -----------------------------------------------
        ''')