def fibo(n):
    x=0
    y=1
    z=1
    print(x,y ,end=" ")
    for z in range(1,n-1):
        z=x+y
        print(z , end=" ")
        x=y
        y=z

print("Program to find n fibonacci numbers.")
n=int(input("PLease enter the limit:  "))
fibo(n)
