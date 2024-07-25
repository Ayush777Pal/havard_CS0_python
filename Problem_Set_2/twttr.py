text=input("Input: ")
text_2=""
for char in text:
    if char in ["A","E","I","O","U","a","e","i","o","u"]:
        text_2 = text_2
    else:
        text_2+=char

print(f"Output:{text_2}")
