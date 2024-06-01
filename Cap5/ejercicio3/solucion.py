valores = []
suma = 0
promedio = 0

for i in range(4):
    valores.append(int(input(f"{i + 1} Ingrese un numero:")))
    
for j in range(len(valores)):
    suma += valores[j]
    promedio = suma / 4
    
print(f"La suma de los valores es: {suma} \n El promedio de la suma es: {promedio}")
    