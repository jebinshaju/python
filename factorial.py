def facto(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print("...Factorial of a nuber...")
n=int(input("Enter the nuber  :"))
print("The factorial is",facto(n))
    
