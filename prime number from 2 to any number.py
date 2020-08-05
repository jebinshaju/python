print("Program to print prime numbers from 2.")
def prime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            break
    else:
        print(x)
            
while True:
    n=int(input("Enter your lower limit:: "))
    for i in range(2,n+1):
        prime(i)
    print("Thank you!!!")
    op=input("To conitnue enter y ,To exit enter n::::  ")
    if op=="n":
        break
