import os
import random
import time

# Global constants for better practice
USER_DATA = {}

class DataProcessor:
    def __init__(self):
        self.config = {
            "api_key": "default_key",
            "retry_count": 3,
            "timeout": 5
        }

    def fetch_with_retries(self, i, retries=3):
        data = self.fetch_data(i)
        attempts = 1
        while not data and attempts <= retries:
            print(f"Retrying {i}... Attempt {attempts}")
            data = self.fetch_data(i)
            attempts += 1
        return data

    def process_data(self, data, i):
        if data:
            print(f"Processed {i}: {data}")
            USER_DATA[i] = data
        else:
            print(f"Failed to process {i}.")

    def process_all_data(self):
        for i in range(10):
            data = self.fetch_with_retries(i)
            self.process_data(data, i)
        return USER_DATA

    def fetch_data(self, i):
        # Simulating a random failure with a 20% chance
        if random.random() < 0.2:  # 20% failure rate
            return None
        return f"data_{i}"

def main():
    processor = DataProcessor()
    processor.process_all_data()

if __name__ == "__main__":
    main()
