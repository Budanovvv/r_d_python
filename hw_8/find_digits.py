text_example = "The recipe calls for 2 cups of flour, 1/2 cup of sugar, and 3 eggs."


def check(symbol):
    if symbol.isdigit():
        return symbol.isdigit()


def find_digits(data):
    digits = []
    for e in filter(check, data):
        digits.append(e)
    print(f"Founded digits {digits}")
    return digits


find_digits(text_example)

# Second variant
# for e in filter(lambda d: d.isdigit(), text_example):
#     print(e)
