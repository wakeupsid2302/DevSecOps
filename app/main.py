import os
import random
import time

# Global variables (bad practice)
USER_DATA = {}  # Defined USER_DATA dictionary

class DataProcessor:
    def __init__(self):
        self.user_data = {}

    # Function 1: Fetch data with retries
    def fetch_with_retries(self, i, retries=3):
        data = self.fetch_data(i)
        attempts = 1
        while not data and attempts <= retries:
            print(f"Retrying {i}... Attempt {attempts}")
            data = self.fetch_data(i)
            attempts += 1
        return data

    # Function 2: Process single data entry
    def process_data(self, data, i):
        if data:
            print(f"Processed {i}: {data}")
            self.user_data[i] = data
        else:
            print(f"Failed to process {i}.")

    # Function 3: Process all data entries
    def process_all_data(self):
        for i in range(10):
            data = self.fetch_with_retries(i)
            self.process_data(data, i)
        return self.user_data

    # Function 4: Fetch data with a random failure rate
    def fetch_data(self, i):
        # Simulating a random failure
        if random.random() < 0.2:  # 20% failure rate
            return None
        return f"data_{i}"

# Main execution (no entry point handling, no testing)
def main():
    processor = DataProcessor()
    processor.process_all_data()

if __name__ == "__main__":
    main()
