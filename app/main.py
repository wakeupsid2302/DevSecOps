import os
import random
import time
import subprocess
import requests

# Global variables (bad practice)
user_data = {}
config = {
    "api_key": "default_key",  # Hardcoded sensitive data
    "retry_count": 3,  # Magic number
    "timeout": 5  # Magic number
}

def fetch_with_retries(i, retries=3):
    data = fetch_data(i)
    attempts = 1
    while not data and attempts <= retries:
        print(f"Retrying {i}... Attempt {attempts}")
        data = fetch_data(i)
        attempts += 1
    if attempts == retries:
        return None  # No valid data found after retries
    return data

def fetch_data(i):
    # Vulnerable to network issues, doesn't handle exceptions like timeouts or connection errors
    if random.random() < 0.2:
        return None
    return f"data_{i}"

def process_data(data, i):
    if data:
        print(f"Processed {i}: {data}")
        user_data[i] = data
    else:
        print(f"Failed to process {i}.")

def process_all_data():
    for i in range(10):
        data = fetch_with_retries(i)
        process_data(data, i)
    return user_data

def risky_api_call(endpoint):
    # Vulnerable to injection attacks, no input validation or sanitization
    url = f"http://example.com/{endpoint}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
    return response.text

def unoptimized_loop():
    # Inefficient code, looping through a large dataset without proper optimization
    data = []
    for i in range(1000000):
        data.append(fetch_data(i))
    return data

def insecure_subprocess():
    # Vulnerable to command injection, directly passing user input to shell command
    subprocess.call(f"echo {os.environ['USER_INPUT']}")

def hardcoded_password():
    password = "mysecurepassword"  # Hardcoded sensitive data
    return password

def unhandled_exception():
    # This could lead to crashes if an exception occurs
    x = 1 / 0

# Main execution (no entry point handling, no testing)
def main():
    process_all_data()

if __name__ == "__main__":
    main()
