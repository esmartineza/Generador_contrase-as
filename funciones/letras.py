import random
from funciones.gen_letras import gen_letras
from funciones.gen_numeros import gen_numeros
from funciones.gen_simbolos import gen_simbolos
from funciones.gen_random import gen_random

def letras():
    print("Generar contraseña aleatoria")
    print('''Seleccione una opcion 
        1.solo letras(Max 54)
        2.solo numeros(Max 10)
        3.Solo Simbolos(Max 26)  
        4.Contraseña aleatoria(Max 88)
        5.Salir
        ''')  
    opciones = int(input("Seleccione una de las opciones: "))
    if opciones == 1:
        gen_letras()
    elif opciones == 2:
        gen_numeros()
    elif opciones == 3:   
        gen_simbolos()
    elif opciones == 4:
        gen_random()
    else:
        print("Salio del Generador de Contraseñas")