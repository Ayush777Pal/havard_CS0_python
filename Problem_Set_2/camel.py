text=input("camelCase: ")
snake_case_text=""
for char in text:
    if char.isupper():
        snake_case_text+= "_" + char.lower()
    else:
        snake_case_text+= char

snake_case_text=snake_case_text.strip("_")
print("snake_case:"+ snake_case_text)
