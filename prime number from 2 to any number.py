def prime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            break
    else:
        print(x)
            
n=int(input("Enter your lower limit:: "))
for i in range(2,n+1):
    prime(i)
