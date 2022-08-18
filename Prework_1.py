
# Question one: Make a function to prinout hello_USERNAME

def hello_name(username):
    print("hello_" + username.upper() + "!")
# used the parameter plus the upper method to capitalize USERNAME


# Then since the question used the same word for the parameter and arguement I just called the function using the parameter as a string
hello_name('username')

# Question 2
# This is how we qould do it if it wasn't a function
for num in range(1, 101):
    if num % 2 != 0:
        print(num)
# For a function we'd have to do it differently
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds(numbers):
    odd = []  # create an empty list
    number = 1 # start of range
    while number <= numbers: # given the while loop a break point to be defined later
        if number % 2 == 1: # establishing we want the odd numbers with modulo symbol and set it = 1
            odd.append(number) # taking out the odd numbers
        number = number + 1 # adding a number to the loop
    print(odd)
    if number % 2 == 0:
        print("None")


numbers = 100  # define the final number or break for the loop

first_odds(numbers)


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_list(a_list):
    print(max(a_list))

list_1 = [5, 7, 11, 99, 101]

max_num_list(list_1)

# Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. # The return should be boolean Type (true/false).

def is_leap_year(a_year):
    year = a_year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap year")

year = 1868

is_leap_year(year)


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive # numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))


list1 = [2, 3, 4, 5, 6, 7]
list2 = [1, 2, 4, 5]

is_consecutive(a_list=list2)
is_consecutive(a_list=list1)
# This does not run unless you right click and select run selected lin python terminal, Maybe because Question 3 has the the same parameter?
