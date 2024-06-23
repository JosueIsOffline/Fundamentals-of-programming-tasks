# Josue Hernandez 2024-0235

import os
PASSWORD = "admin"
intentos = 3


user = input("Ingresa tu usuario: ")
password = input("Ingresa tu clave: ")

if password != PASSWORD:
        intentos -= 1
        print(f"Clave incorrecta, te quedan {intentos} intentos")
elif password == PASSWORD: 
    os.system("cls")
    print("Bienvenido")

while(password != PASSWORD and intentos > 0):
    password = input("Intenta ingresar tu clave nuevamente: ")
    
    if password != PASSWORD:
        intentos -= 1
        print(f"Clave incorrecta, te quedan {intentos} intentos")
    elif password == PASSWORD: 
        os.system("cls")
        print("Bienvenido")
        break
    
print("Has ingresado la clave mal varias veces. Intentalo mas tarde")

