import time
from datetime import datetime, timedelta
import importlib
def schedule_jobs(file_path,job_module):  # Added the missing comma here
    # Read the jobs from the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        job_name, condition = line.strip().split(",")
        
        # Calculate when to run the job
        if condition.endswith("s"):
            delay = int(condition[:-1])  # Seconds
        elif condition.endswith("m"):
            delay = int(condition[:-1]) * 60  # Minutes
        else:
            print(f"Invalid condition: {condition}")
            continue
        
        # Wait until the job's time
        print(f"Scheduled {job_name} to run in {delay} seconds.")
        time.sleep(delay)
        
        # Run the job
        job_func = getattr(importlib.import_module(job_module), job_name)
        print(f"Running {job_name} at {datetime.now().strftime('%H:%M:%S')}")
        job_func()
