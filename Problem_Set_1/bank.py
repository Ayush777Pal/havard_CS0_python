def main():
  n=input("Greeting: ")
  b=n.lower().replace(" ","")
  check(b)

def check(b):
  if b=="hello":
     print("$0")
  elif b[0]=="h":
     print("$20")
  else:
     print("$100")

main()