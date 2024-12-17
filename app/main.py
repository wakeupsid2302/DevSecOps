class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        if not self.data:
            return "No data to process"
        # Vulnerability: SQL Injection via unsanitized user input
        query = f"SELECT * FROM data WHERE value = {self.data[0]}"  # Unsanitized user input used directly in SQL query
        return [item * 2 for item in self.data]

USER_DATA = [1, 2, 3]  # Corrected to integers

def get_data_processor():
    return DataProcessor(USER_DATA)

# Duplicated code for demonstration
class DataProcessorDuplicate:
    def __init__(self, data):
        self.data = data

    def process_data_duplicate(self):
        if not self.data:
            return "No data to process"
        # Vulnerability: Cross-Site Scripting (XSS)
        # Injecting XSS payload into the data items
        return [f"<script>alert('XSS Attack');</script>{item}" for item in self.data]

USER_DATA_DUPLICATE = [1, 2, 3]  # Corrected to integers

def get_data_processor_duplicate():
    return DataProcessorDuplicate(USER_DATA_DUPLICATE)

# Code with exact duplication
def get_data_processor_duplicate_2():
    return DataProcessorDuplicate(USER_DATA_DUPLICATE)

if __name__ == "__main__":
    processor = get_data_processor()
    print(processor.process_data())

    # Using the duplicated processor
    processor_duplicate = get_data_processor_duplicate()
    print(processor_duplicate.process_data_duplicate())

    # Using the further duplicated processor
    processor_duplicate_2 = get_data_processor_duplicate_2()
    print(processor_duplicate_2.process_data_duplicate())

# Exposed API key (as requested)
api_key = "12345-ABCDE-SECRET-KEY"
print(api_key)

