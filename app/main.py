import os
import random

# Configuration (use environment variables for sensitive data)
config = {
    "api_key": os.getenv("API_KEY", "default_key"),  # Using env variable for secrets
    "retry_count": 3,
    "timeout": 5
}

# Function to simulate fetching data (with error handling)
def fetch_data(i):
    """Simulate data fetching with a random failure."""
    try:
        if random.random() < 0.2:  # 20% failure rate
            raise Exception(f"Failed to fetch data for {i}")
        return f"data_{i}"
    except Exception as e:
        print(e)
        return None

# Refactored function for handling retries
def fetch_with_retries(i, retries):
    """Attempt to fetch data with retries."""
    attempts = 0
    while attempts < retries:
        data = fetch_data(i)
        if data:
            return data
        attempts += 1
        print(f"Retrying {i}, attempt {attempts}...")
    return None

# Function for processing data (separated concerns)
def process_data(data, i):
    """Process the data fetched for each item."""
    if data:
        print(f"Processing data for {i}: {data}")
    else:
        print(f"Could not process data for {i}")

# Main logic for processing data (modularized)
def process_all_data():
    """Process data with retries."""
    user_data = {}
    retries = config["retry_count"]
    for i in range(10):
        data = fetch_with_retries(i, retries)
        user_data[i] = data
        process_data(data, i)
    return user_data

# Main function to run the program
def main():
    print("Starting data processing...")
    user_data = process_all_data()
    print("Data processing completed.")
    return user_data

if __name__ == "__main__":
    main()
