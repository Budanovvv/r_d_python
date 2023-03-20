def describe_str_symbol(text):
    for char in text:
        if char.isdigit():
            if int(char) % 2 == 0:
                print(f"The character {char} is a paired number")
            else:
                print(f"The character {char} is not a pair number")
        elif char.isalpha():
            if char.islower():
                print(f"The character {char} is a lowercase letter")
            else:
                print(f"The character {char} is a uppercase letter")
        elif not char.isalpha() and not char.isalpha():
            print(f"The character {char} is symbol")


input_text = input("Type your text: ")
describe_str_symbol(input_text)
