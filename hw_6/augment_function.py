# Define a function called that takes a variable number of tuples as its argument.
def augment_function(*rnd_numb: tuple):
    # Initialize a variable called 'summ' to 0.
    summ = 0
    # Loop over each tuple in the argument and add up its values.
    for numb in rnd_numb:
        summ = summ + numb
    # Return the total sum of all the values in the argument.
    return summ


# Create a list of numbers from 0 to 9 using the 'range()' function and convert it to a list.
random_numbers = list(range(10))

# Call the function with the contents of the 'random_numbers' list unpacked as arguments,
summ_of_range = augment_function(*random_numbers)

# Print the value of the 'summ_of_range' variable to the console.
print(summ_of_range)
