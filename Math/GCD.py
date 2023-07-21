# GCD and HCF of two numbers
# Euclidean Algorithm Code

def gcd(a,b):
    while a != b:
        if a > b :
            a = a - b
        else :
            b = b - a 
    return a

# Optimised Euclidean Algorithm Code
def gcd(a,b):
    if b == 0 :
        return a
    return gcd(b, a % b)

a = 12
b = 15
print(gcd(a,b))
