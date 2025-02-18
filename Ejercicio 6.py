n = int(input("Ingrese número: ")) 
d1 = n // 100 
d2 = (n // 10) % 10 
d3 = n % 10 
n_inv = d3 * 100 + d2 * 10 + d1 
print("El numero de manera invertida es:",n_inv)