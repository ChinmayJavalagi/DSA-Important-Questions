#i/p: x = 9253
#o/p: 4

x = int(input("Enter x:\n"))
res = 0
while x>0:
    x=x//10
    res = res + 1
print("count of digit is :",res)
