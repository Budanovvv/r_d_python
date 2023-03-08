# import datetime module
import datetime

# make var of name and birthday
birthday = datetime.date(1984, 3, 13)
my_name = "Valentine"

# calculate the number of months of my life based on the fact that the average month has 30 days.
current_date = datetime.datetime.today().date()  # make var of the current date
age_in_days_datetime = current_date - birthday  # calculate days of my life
age_in_days_str = str(age_in_days_datetime).split()[0]  # age_in_days_datetime from datetime to string, take only days
age_in_days = int(age_in_days_str)  # age_in_days_str from string to int
age_in_month = age_in_days / 30   # float. based on the fact that the average month has 30 days
age_in_years = int(age_in_month / 12)  # int not float. based on the fact that the year has 12 months


# Function which print name and age
def print_age(name, age):
    return print(f"Му name is {name} I’m {age} years old")


# Call the function
print_age(my_name, age_in_years)
