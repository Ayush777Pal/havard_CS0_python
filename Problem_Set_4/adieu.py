import inflect

comma=inflect.engine()
Name=[]
while True:
    try:
        m=input("Name: ")
        Name.append(m.strip())
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to{comma.join(Name)}")
