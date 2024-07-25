def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2<=len(s)<=6 and s[0:2].isalpha() and s.isalnum():#isalum tells that first aplhabet will come then numeric
        for i in s:
            #to only check if first number is not zero
            if i.isdigit():
                #finding value of s in index i
                result=s.index(i)
                #s[result:]gives value present at result
                if s[result:].isdigit() and int(i)!=0:
                   return True
                else:
                    return False
    return True
                
    



main()