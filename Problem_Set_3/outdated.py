mon=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

while True:
    a= input("Date: ")
    try:
        if "/" in a:
            month,day,year=a.split("/")
            if 1<=int(month)<=12 and 1<=int(day)<=31:
                break
        elif "," in a:
            a= a.replace("," , "")
            month,day,year = a.split(" ")
            if month in mon and int(day)<=31:
                month=mon.index(month)+1
                break
    except:
        print()
        pass

print(f"{int(year)}-{int(month):02}-{int(day):02}")
