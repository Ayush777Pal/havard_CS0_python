def main():
     n=input("Greeting: ")
     b=n.lower().replace(" ","")
     print(value(b))


def value(greeting):
    if greeting=="hello":
      return "$0"
    elif greeting[0]=="h":
      return "$20"
    else:
      return "$100"



if __name__ == "__main__":
    main()