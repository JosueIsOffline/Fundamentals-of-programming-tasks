nums = []
for i in range(4):
    nums.append(int(input(f"{i + 1} Ingresa un numero:")))
    
suma = nums[0] + nums[1]
producto = nums[2] * nums[3]

print(f"El resultado de la suma de {nums[0]} + {nums[1]} es: {suma}")
print(f"El resultado del producto de {nums[2]} * {nums[3]} es: {producto}")
