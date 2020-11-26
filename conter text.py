print("Text file counter")
f=open("hai.txt","w")
u=input("Enter some sentences: ")
f.write(u)
f.close()
f=open("hai.txt","r")
y=f.read()
c=0
l=0
d=0
for i in y:
    if i.isupper():
        c=c+1
    elif i.islower():
        l=l+1
    elif i.isdigit():
        d=d+1
print("No of upper case letters:",c,"No of lower case letters:",l,"No of digits:",d)
        
