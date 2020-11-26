print("Check words with 4 characters in string")
q=input("Enter the string to check: ")
q=q.split()
for i in q:
    if len(i)==4:
        print(i)
