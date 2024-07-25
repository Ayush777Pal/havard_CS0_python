from random import randint

while True:
    n=int(input("Level: "))
    try:
        if n<=0:
          raise ValueError
        break
    except ValueError:
       pass

r=randint(1,n)

while True:
  try:
     g=int(input("Guess: "))
     if g==r:
        print("Just Right")
        break
     elif g<r:
        print("Too small")
     else:
        print("Too Large")
  except ValueError:
     pass
    