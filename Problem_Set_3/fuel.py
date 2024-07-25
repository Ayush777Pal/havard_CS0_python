def main():
    x=get_res()
    print(x)

def get_res():
    while True:
        try:
          a=input("Fraction: ").split("/")
          b=float((int(a[0]) / int(a[1]))*100)
          if a[0]<=a[1]:
            if b>=99:
               print("F")
            elif b<=1:
               print("E")
            else:
               print(f"{round(float(b))}%")
               exit()
          else:
             return get_res()
        except((ValueError, ZeroDivisionError)):
           continue 


main()