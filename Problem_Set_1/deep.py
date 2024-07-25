def main():
  i=(input("What is the Answer to the Great Question of Life, the Universe and Everything? "))
  check(i)


def check(i):
    if i=="42":
      print("Yes")
    elif i=="forty-two":
      print("Yes")
    elif i=="Forty Two":
      print("Yes")
    else:
      print("No")

main()