# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    # TODO: Implement this function
    pass  # Replace with your code
    max = 0
    if (num1 > num2):
        max = num1
    else:
        max = num2
    if (max > num3):
        return max
    else:
        return num3

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    # TODO: Implement this function
    pass  # Replace with your code
    pass  # Replace with your code
    min = 0
    if (num1 < num2):
        min = num1
    else:
        min = num2
    if (min < num3):
        return min
    else:
        return num3

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    # TODO: Implement this function
    pass  # Replace with your code
    if (number > 0):
        return "Positive"
    elif (number < 0):
        return "Negative"
    else:
        return "Zero"

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    # TODO: Implement this function
    pass  # Replace with your code
    result = ""
    for i in range(rows):
        for j in range(i + 1):
            result += "*" 
        result += "\n"
    return result.strip()

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    # TODO: Implement this function
    pass  # Replace with your code
    count = 1
    num = ""
    while count <= limit:
        if count%3 == 0:
            num += "Multiple of 3" + "\n"
        else:
            num += str(count) + "\n"
        count += 1
    return num.strip()

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    # TODO: Implement this function
    pass  # Replace with your code
    count = start
    num = 0
    while count <= end:
        if count%2 == 0:
            num += count
        count += 1
    return num

    
#6. **(20%)** Do-While Loop Simulation – Ask for Positive Number:
#- Write a function that continuously asks the user for a number until they input a positive number. The function should return the first positive number input by the user.

#def first_positive_number(number):
    #num = 0
    #if number%2 == 0:
        #num += number
    #else:
        #...