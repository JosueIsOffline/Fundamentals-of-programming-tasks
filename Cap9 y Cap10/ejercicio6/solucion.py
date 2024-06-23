# Josue Hernandez 2024-0235
import os


nombre = input("Ingresa el nombre del empleado: ")
cedula = input(f"Ingresa la cedula de {nombre}: ")
cargo = input("Ingresa el cargo: ") 

sueldo_bruto = float(input("Ingrese el sueldo bruto: "))

seguro_social = 0.05 * sueldo_bruto
fondo_pension = 0.04 * sueldo_bruto

exceso_4000 = 0
impuesto_renta = 0

if sueldo_bruto >= 40000:
    exceso_40000 = sueldo_bruto - 40000
    impuesto_renta = 0.10 * exceso_40000
else:
    impuesto_renta = 0
    

gasto_presentacion = 0
if cargo.lower() == "gerente":
    gasto_presentacion = 10000
    
total_descuento = seguro_social + fondo_pension + impuesto_renta

sueldo_neto =  sueldo_bruto + gasto_presentacion - total_descuento

os.system("cls")

print(f"Nombre del empleado: {nombre} \nCedula: {cedula} \nCargo: {cargo} \n")

print(f"Sueldo bruto: {sueldo_bruto} \nSeguro social: {seguro_social} \nFondo de pension: {fondo_pension} \nImpuesto a la renta: {impuesto_renta} \nGasto de presentacion: {gasto_presentacion} \nTotal descuento: {total_descuento} \nSueldo neto: {sueldo_neto}")