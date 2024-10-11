# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#
def car_at_light(light):
    if light == "red":
        return "stop"
    elif light == "green":
        return "go"
    elif light == "yellow":
        return "wait"
    else:
        raise Exception(f"Undefined instruction for color: {light}")


# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 

def safe_subtract(a, b):
    try:
        return a - b
    except TypeError:
        # If there's a type issue, return None
        return None
    except Exception as e:
        # For any other type of issue, print the error and return None
        print(f"An error occurred: {e}")

#3)
#  Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl
from datetime import datetime

def retrieve_age_eafp(person):
    current_year = datetime.now().year
    try:
        birth_year = person['birth']
        return current_year - birth_year
    except KeyError:
        return "Birth year is not available."

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

def read_data(file_path="data.csv"):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None

# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double  # Add double instead of elem


### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

strings = ''
for string in ['I', 'am', 'Groot']:
    strings += string + "_"  # Accumulate the strings with an underscore
strings = strings.rstrip('_')  # Remove the last unnecessary underscore

### (c) Careful!
j=10
while j > 0:
   j += 1

j = 10
while j > 0:
    j -= 1  # Decrement j to eventually break the loop


### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem

productory = 1  # Start with 1 for a product
for elem in [1, 5, 25]:
    productory *= elem



