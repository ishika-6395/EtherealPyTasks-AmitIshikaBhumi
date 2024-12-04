# main.py

from datetime import datetime, timedelta
from jobs import (
    job_hello, job_bye, job_print_numbers, job_print_letters,
    job_reverse_string, job_sum_numbers, job_multiply,
    job_greet_user, job_calculate_square, job_display_time
)
from scheduler import schedule_jobs

if __name__ == "__main__":
    # Define jobs and their schedule times
    jobs_with_times = [
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

    # Schedule and execute jobs
    schedule_jobs(jobs_with_times)
