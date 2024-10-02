primos = [] 

for i in range(1, 250):
    if i > 1:
        count = 0
        j = 2
        while j < i and count == 0:
            numeros = i % j
            if numeros == 0:
                count += 1 
            j += 1
        if count == 0:
            print(i, end=", ")  
            primos.append(i)  

with open('results.txt', 'w') as file:
    file.write("Números primos entre 1 y 250:\n")
    for numero in primos:
        file.write(f"{numero}\n")

print(f"\nLos números primos entre 1 y 250 han sido escritos en 'results.txt'.")
