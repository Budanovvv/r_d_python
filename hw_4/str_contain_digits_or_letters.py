# Make function to compare data type of string
def match_data_type(data):
    if data.isdigit():  # Try to find only digits
        print("Data -> Contain only digits")
        if int(data) % 2 == 0:  # Check that digit is a double number
            print("Digit -> Double number")
        else:
            print("Digit -> Undouble number")
    elif data.isalpha():  # Try to find only letters
        print("Data -> Contain only letters")
    elif data.isalnum():  # Try to find only letters and digits
        print("Data -> Contain letters and digits")
    else:  # Exception if finding something other than letters and digits
        print(f"I don't expect this kind of data -> {data}")


# Input data ro compare
input_text = input("Print your data -> ")

# Call function to compare entered data
match_data_type(input_text)
