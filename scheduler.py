# scheduler.py

from datetime import datetime, timedelta
import time

def schedule_jobs(jobs_with_times):
    print("Starting job scheduling...\n")
    for job, schedule_time in jobs_with_times:
        while datetime.now() < schedule_time:
            time.sleep(1)  # Wait until the scheduled time
        print(f"Job started at {datetime.now().strftime('%H:%M:%S')}")
        job()  # Execute the job function
        print(f"Job completed at {datetime.now().strftime('%H:%M:%S')}\n")
    print("All jobs have been successfully completed.")
