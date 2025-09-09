#Este ejercicio vale una decima para el primer corte, clase 09/09/2025
try:
    while True:
        try:
            value = int(input("Ingresa un número, (Ctrl + c para salir):"))

            for i in range(1,value+1):
                conta = 0
                for n in range(1, i+1):
                    residue = i%n
                    if residue == 0:
                        conta = conta + 1
                    
                
            if conta == 2:
                print(f'{i} es un primo')
                print("\n")
            else:
                print(f'{i} No es un numero primo')
                print("\n")

            
        except ValueError:
            print("Incorrecto, ingrese un número")
except KeyboardInterrupt:
    print("\n\n Programa terminado")
    