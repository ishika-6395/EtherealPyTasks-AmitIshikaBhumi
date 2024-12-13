from scheduler import schedule_jobs
import job_bye
import job_greet_user
import job_hello
import job_multiply
import job_print_letters
import job_print_numbers
import job_reverse_string
import job_calculate_square
import job_sum_numbers
import job_display_time

if __name__ == "__main__":
    # List of all job functions to execute
    all_jobs = [
        job_hello.job_hello,
        job_bye.job_bye,
        job_print_numbers.job_print_numbers,
        job_print_letters.job_print_letters,
        job_reverse_string.job_reverse_string,
        job_sum_numbers.job_sum_numbers,
        job_multiply.job_multiply,
        job_greet_user.job_greet_user,
        job_calculate_square.job_calculate_square,
        job_display_time.job_display_time
    ]
    
    # Run each job function
    for job in all_jobs:
        job()
