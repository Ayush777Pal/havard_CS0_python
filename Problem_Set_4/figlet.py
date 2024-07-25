import sys
from pyfiglet import Figlet
import random

lis=Figlet().getFonts()
if len(sys.argv)==1:
    li=random.choice(lis)
elif len(sys.argv)==3:
        if sys.argv[1]in ["-f","--font"] and sys.argv[2]in lis:
            li=sys.argv[2]
        else:
            sys.exit("invalid expression")
else:
     sys.exit("no input")

text=input("Input: ")
print("Output: ", Figlet(font=li).renderText(text))
    