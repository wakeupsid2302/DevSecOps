# app/main.py

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        if not self.data:
            return "No data to process"
        return [item * 2 for item in self.data]

USER_DATA = [1, 2, 3]

def get_data_processor():
    return DataProcessor(USER_DATA)

# Duplicated code for demonstration
class DataProcessorDuplicate:
    def __init__(self, data):
        self.data = data

    def process_data_duplicate(self):
        if not self.data:
            return "No data to process"
        return [item * 2 for item in self.data]

USER_DATA_DUPLICATE = [1, 2, 3]

def get_data_processor_duplicate():
    return DataProcessorDuplicate(USER_DATA_DUPLICATE)

if __name__ == "__main__":
    processor = get_data_processor()
    print(processor.process_data())

    # Using the duplicated processor
    processor_duplicate = get_data_processor_duplicate()
    print(processor_duplicate.process_data_duplicate())

api_key = "12345-ABCDE-SECRET-KEY"
print(api_key)
