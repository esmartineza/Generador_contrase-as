print("calculadora")
print('''
1.comenzar
''')
comenzar = input("seleccione una de las opciones:")
while True:
    if comenzar !=5:
        print('''
        |------------------------------------|
        |1.Sumar                             |
        |2.Restar                            |
        |3.Multiplicar                       |
        |4.Dividir                           |
        |5.Calcular Edad                     |
        |6.Salir                             |
        |------------------------------------|        
        ''')
        dato = input("seleccione una de las opciones:")
        if dato == "1":
            numero1 = int(input("ingrese primer numero: "))
            numero2 = int(input("ingrese segundo numero: "))
            suma = numero1 + numero2
            print("la suma es: ", suma)
        if dato == "2":
            numero1 = int(input("ingrese primer numero: "))
            numero2 = int(input("ingrese segundo numero: "))
            resta = numero1 - numero2
            print("la resta es: ", resta)
        if dato == "3":
            numero1 = int(input("ingrese primer numero: "))
            numero2 = int(input("ingrese segundo numero: "))
            multiplicar = numero1 * numero2 
            print("la multilpicacion es: ", multiplicar) 
        if dato == "4":
            numero1 = int(input("ingrese primer numero: "))
            numero2 = int(input("ingrese segundo numero: "))
            dividir  = numero1 / numero2 
            print("la dividir es: ",dividir) 
        if dato == "5":
            numero1 = int(input("ingrese su año de nacimiento: "))
            calculo = 2022 - numero1 
            print("usted tiene: ",calculo)
        print("¿desea continuar?")
        respuesta  = input().upper()
        if respuesta == "SI":
            print("continuar")
        else:
            print("calculadora finalizada")
            break            

