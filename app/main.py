# app/main.py

import os
import random
import time

# Global variables (bad practice)
user_data = {}
config = {
    "api_key": "default_key",
    "retry_count": 3,
    "timeout": 5
}

# Function 1: Poorly named function, unclear purpose
def f1():
    global user_data
    for i in range(10):  # Duplicated logic
        data = fetch_data(i)
        user_data[i] = data
        time.sleep(1)  # Simulating delay without reason

# Function 2: Long function, too many responsibilities
def f2():
    global user_data
    api_key = os.getenv("SECRET_API_KEY", "default_secret")  # Hardcoded secret
    retry_count = config["retry_count"]
    
    for i in range(10):
        data = fetch_data(i)  # Duplicate data fetching logic
        if not data:
            if retry_count > 0:
                print(f"Retrying to fetch data for {i}... {retry_count} retries left.")
                retry_count -= 1
                data = fetch_data(i)
            else:
                print(f"Failed to fetch data for {i}. Moving to next.")
        user_data[i] = data
        time.sleep(1)  # Unnecessary delay

# Function 3: Another long function with similar logic
def f3():
    global user_data
    api_key = os.getenv("SECRET_API_KEY", "default_secret")  # Hardcoded secret
    retry_count = config["retry_count"]
    
    for i in range(10):
        data = fetch_data(i)  # Duplicated logic
        if data:
            user_data[i] = data
        else:
            print(f"Error fetching data for {i}.")
        time.sleep(1)  # Unnecessary delay

# Function 4: Fetching data with no error handling or validation
def fetch_data(i):
    # Simulating a random failure
    if random.random() < 0.2:  # 20% failure rate
        print(f"Failed to fetch data for {i}")
        return None
    return f"data_{i}"

# Function 5: Mixing concerns
def f4():
    print("Starting process...")
    for i in range(10):
        print(f"Processing {i}...")
        data = fetch_data(i)
        if data:
            print(f"Data for {i}: {data}")
        else:
            print(f"Could not process {i}")
        time.sleep(1)  # Unnecessary delay

# Main execution (no entry point handling, no testing)
def main():
    f1()
    f2()
    f3()
    f4()

if __name__ == "__main__":
    main()

