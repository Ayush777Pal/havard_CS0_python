def main():
    fuel=input("Enter fraction:")
    per=convert(fuel)
    cond=gauge(per)
    print(cond)

def convert(fraction):
    a= fraction.split("/")
    x=int(a[0])
    y=int(a[1])
    if x/y>1:
            raise ValueError
    elif y==0:
            raise ZeroDivisionError
    else:
            return round(float(x/y)*100)

def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return percentage

    


if __name__ == "__main__":
    main()