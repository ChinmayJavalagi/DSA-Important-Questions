# Palindrome number
# Create another number by always taking the last digit of the n and atlast compare if they are equal.

def ispal(n) :
    rev = 0
    temp = n
    while temp != 0 :
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    if (rev == n) :
        print(True)
    else :
        print(False)
    
x = 789987
ispal(x)
