a=50
b=a
while(b!=0):
    print(f"Amount Due: {b}")
    due=int(input("Insert coin: "))
    b=b-due

print("Change Owed:", b)
