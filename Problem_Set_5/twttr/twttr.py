def main():
    text=input("Input: ")
    print("output:",shorten(text))


def shorten(word):
    text_2=""
    for char in word:
        if char in ["A","E","I","O","U","a","e","i","o","u"]:
            text_2 = text_2
        else:
            text_2+=char
    return f"{text_2}"

if __name__ == "__main__":
    main()