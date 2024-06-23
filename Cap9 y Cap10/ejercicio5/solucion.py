# Josue Hernandez 2024-0235

import os

def obtener_literal(promedio):
    if 90 <= promedio <= 100:
        return 'A'
    elif 80 <= promedio < 90:
        return 'B'
    elif 70 <= promedio < 80:
        return 'C'
    elif promedio <= 60:
        return 'F'
    


nombre = input("Ingresa el nombre del estudiante: ")
matricula = input(f"Ingresa la matricula de {nombre}: ")
asignatura = input("Ingresa la asignatura: ")

calificaciones = []
for i in range(4):
    calificacion = float(input(f"Ingrese la calificacion {i+1}: "))
    calificaciones.append(calificacion)
    
    
    
os.system("cls")

print(f"Nombre del estudiante: {nombre} \nMatricula: {matricula} \nAsignatura: {asignatura} \n")    

for j in range(len(calificaciones)):
    print(f"Calificacion {j+1}: {calificaciones[j]}")
    
    
promedio = round(sum(calificaciones) / len(calificaciones), 2)

print(f"El estudiante tiene una {obtener_literal(promedio)} literal con un promedio de {promedio}")
