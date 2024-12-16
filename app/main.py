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

# Function 1: Fetch data with retries
def fetch_with_retries(i, retries=3):
    data = fetch_data(i)
    attempts = 1
    while not data and attempts <= retries:
        print(f"Retrying {i}... Attempt {attempts}")
        data = fetch_data(i)
        attempts += 1
    return data

# Function 2: Process single data entry
def process_data(data, i):
    if data:
        print(f"Processed {i}: {data}")
        user_data[i] = data
    else:
        print(f"Failed to process {i}.")

# Function 3: Process all data entries
def process_all_data():
    for i in range(10):
        data = fetch_with_retries(i)
        process_data(data, i)
    return user_data

# Function 4: Fetch data with a random failure rate
def fetch_data(i):
    # Simulating a random failure
    if random.random() < 0.2:  # 20% failure rate
        return None
    return f"data_{i}"

# Main execution (no entry point handling, no testing)
def main():
    process_all_data()

if __name__ == "__main__":
    main()
