def main():
    time=input("What time it is? ")
    meal=convert(time)
    if 7<=meal<=8:
        print("breakfast time")
    elif 12<=meal<=13:
        print("lunch time")
    elif 18<=meal<=19:
        print("dinner time")


def convert(time):
    hour,min=time.split(":")
    hour=float(hour)+(float(min)/60)
    return hour


if __name__ == "__main__":
    main()