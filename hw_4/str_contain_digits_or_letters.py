# Make function to compare data type of string
def match_data_type(data):
    if data.isdigit():  # Try to find only digits
        print("Your data contain only digits")
    elif data.isalpha():  # Try to find only letters
        print("Your data contain only letters")
    elif data.isalnum():  # Try to find only letters and digits
        print("Your data contain letters and digits")
    else:  # Exception if finding something other than letters and digits
        print(f"I don't expect this kind of data -> {data}")


# Input data ro compare
input_text = input("Print your data -> ")

# Call function to compare entered data
match_data_type(input_text)
