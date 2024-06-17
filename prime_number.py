#--------- prime numbers -----------
def is_prime(num):
    
# Escribe tu código aquí. 
    if num <=1:
        return False
    if num ==2:
        return True
    if num % 2 ==0:
        return False
    for i in range(3,(num // 2) + 1 ,2):
        if num % i==0:
            return False
            
    return True

 

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
 
