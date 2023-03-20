# Make function to check data type of string symbols by match/case
def check_data_type(data):
    print("===========First option===========")
    match data:
        case data if data.isdigit():
            print("Data -> Contain only digits")
        case data if data.isalpha():
            print(f"Data -> Contain only letters")
        case data if data.isalnum():
            print("Data -> Contain letters and digits")
        case data if data.islower():
            print("Data -> Contain only of lowercase characters")
        case data if data.isupper():
            print("Data -> Contain only of uppercase characters")
        case data if data.isspace():
            print("Data -> Contain only whitespace characters")
        case data if data.isprintable():
            print("Data -> Checks if all characters of a string can be printed \n"
                  " (i.e. does not contain control characters).")
        case _:  # Exception if finding something other than letters and digits
            print(f"I don't expect this kind of data -> {data}")


# Make function to check data type of string symbols, and return more complex description
def check_and_collect_data_type(data):
    print("===========Second option===========")
    description = []
    if data.isalnum():
        if data.isdigit():
            description.append(" - only digits")
        if data.isalpha():
            description.append(" - only letters")
        else:
            description.append(" - letters and digits")
    if data.islower():
        description.append(" - only of lowercase characters")
    if data.isupper():
        description.append(" - only of uppercase characters")
    if data.isspace():
        description.append(" - only whitespace characters")
    if data.isprintable():
        description.append(" - all characters of a string can be printed")
    else:  # Exception if finding something other than letters and digits
        print(f"I don't expect this kind of data -> {data}")
        return

    print("Data description:", *description, sep="\n")


# Input data ro compare
input_text = input("Print your data -> ")

# Call function to compare entered data by match/case
check_data_type(input_text)

# Call function to compare entered data with complex description
check_and_collect_data_type(input_text)
