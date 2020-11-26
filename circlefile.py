import circle
print(" AREA AND PERIMETER OF  A CIRCLE")

while True:
    
    print("1. for area")
    print("2. for perimeter")
    print("3. to exit")
    op=int(input("Enter your option: "))
    
    if op==1:
        r=float(input("Enter the radius of the circle: "))
        print("The area is ",circle.area(r))
        

    if op==2:
        r=float(input("Enter the radius of the circle: "))
        print("The perimeter is : ",circle.perimeter(r))
        
    if op==3:
        break
