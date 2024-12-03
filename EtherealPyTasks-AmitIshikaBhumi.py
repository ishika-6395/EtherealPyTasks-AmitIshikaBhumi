import time
from datetime import datetime, timedelta

# Define different jobs as functions
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
    name = "Ishika"
    print(f"Welcome, {name}!")

def job_calculate_square():
    number = 6
    print(f"Square of {number} is {number ** 2}")

def job_display_time():
    print("Current Time:", time.strftime("%Y-%m-%d %H:%M:%S"))

# Schedule jobs at specific times
def schedule_jobs():
    jobs = [
        (job_hello, datetime.now() + timedelta(seconds=5)),
        (job_bye, datetime.now() + timedelta(seconds=10)),
        (job_print_numbers, datetime.now() + timedelta(seconds=15)),
        (job_print_letters, datetime.now() + timedelta(seconds=20)),
        (job_reverse_string, datetime.now() + timedelta(seconds=25)),
        (job_sum_numbers, datetime.now() + timedelta(seconds=30)),
        (job_multiply, datetime.now() + timedelta(seconds=35)),
        (job_greet_user, datetime.now() + timedelta(seconds=40)),
        (job_calculate_square, datetime.now() + timedelta(seconds=45)),
        (job_display_time, datetime.now() + timedelta(seconds=50)),
    ]

    print("Starting job scheduling...\n")
    for job, schedule_time in jobs:
        while datetime.now() < schedule_time:
            time.sleep(1)  # Wait until the scheduled time
        print(f"Job started at {datetime.now().strftime('%H:%M:%S')}")
        job()
        print(f"Job completed at {datetime.now().strftime('%H:%M:%S')}\n")

    print("All jobs have been successfully completed.")

# Main function
if __name__ == "__main__":
    schedule_jobs()
