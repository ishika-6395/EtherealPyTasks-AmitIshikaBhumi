# jobs.py

import time

def job_hello():
    print("Hello, World!")

def job_bye():
    print("Goodbye!")

def job_print_numbers():
    print("Printing numbers: ", list(range(1, 6)))

def job_print_letters():
    print("Printing letters: ", ["A", "B", "C", "D", "E"])

def job_reverse_string():
    text = "Python"
    print(f"Reversed string: {text[::-1]}")

def job_sum_numbers():
    print(f"Sum of numbers 1 to 10: {sum(range(1, 11))}")

def job_multiply():
    print("Multiplication of 5 x 4 = ", 5 * 4)

def job_greet_user():
    name = "Bhumi"
    print(f"Welcome, {name}!")

def job_calculate_square():
    number = 6
    print(f"Square of {number} is {number ** 2}")

def job_display_time():
    print("Current Time:", time.strftime("%Y-%m-%d %H:%M:%S"))
