
# Josue Hernandez 2024-0235

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    suma = num1 + num2
    diferencia = num1 - num2
    print(f"La suma de {num1} y {num2} es: {suma}")
    print(f"La diferencia entre {num1} y {num2} es: {diferencia}")
else:
    producto = num1 * num2
    if num2 != 0:
        division = num1 / num2
        print(f"El producto de {num1} y {num2} es: {producto}")
        print(f"La división de {num1} entre {num2} es: {division}")
    else:
        print("No se puede dividir por cero.")
