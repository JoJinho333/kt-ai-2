# 4308 해결
n = int(input())

def is_prime_num(n):
    if (n < 2): 
        return 0
    
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return 0 
    
    return 1

print(is_prime_num(n))