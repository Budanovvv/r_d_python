def from_number_to_zero(number):
    print(f"Number => {number}")
    if number == 0:
        return None
    n = number - 1
    return from_number_to_zero(n)


from_number_to_zero(10)
