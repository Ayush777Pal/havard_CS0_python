import random


def main():
    level=get_level()
    score=0
    for _ in range(10):
        x,y=generate_integer(level)
        h=0
        while h<3:
            try:
                num=int(input(f"{x}+{y}="))
                if num==(x+y):
                    score=score+1
                    break
                else:
                    print("EEE")
            except:
                print("EEE")
                pass
            h=h+1
        if h==3:
           print(f"{x}+{y}={x+y}")
    print("Your score"+str( score))
        


def get_level():
    while True:
        try:
           level=int(input("Level: "))
           if level in [1,2,3]:
               break
           else:
               pass
        except:
            pass
    return level
    


def generate_integer(level):
    if level==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
    elif level==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
    else:
        x=random.randint(100,999)
        y=random.randint(100,999)
    return x,y





if __name__ == "__main__":
    main()