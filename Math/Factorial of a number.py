# Factorial of a number
#bruteforce
#TC - 0(n)

def factorial(n):
      
    if n == 0:
        return (1)
    return (n * factorial(n-1))
n = 5
print(factorial(n))
