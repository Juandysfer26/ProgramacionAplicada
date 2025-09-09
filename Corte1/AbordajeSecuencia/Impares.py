#Este ejercicio vale una decima para el primer corte, clase 09/09/2025
try:
   while True:
     try:
        num = int(input("Ingresa un número, (Ctrl + c para salir):"))
        if num % 2 == 0:
            print(f"{num} es par")
            
        else:
            print(f"{num} es impar")
     except ValueError:
         print("Incorrecto, porfavor ingrese un número")
except KeyboardInterrupt:
    print("\n\n Programa terminado")
