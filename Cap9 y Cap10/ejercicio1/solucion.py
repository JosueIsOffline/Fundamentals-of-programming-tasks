def cSuperficie(base, altura):
    return (base * altura) / 2

def main():
    contador = 0
    n = int(input("Ingrese el numero de triangulos:"))
    
    for i in range(n):
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        
        superficie = cSuperficie(base, altura)
        print(f"La superficie del triangulo {i+1} con base = {base} y altura = {altura} es: {superficie}")
        
        if superficie > 12:
            contador += 1
            
    print(f"La cantidad de triangulos con superficie mayor a 12 es: {contador}")
        
    
    
if __name__ == "__main__":
     main()

