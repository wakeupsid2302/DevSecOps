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

if __name__ == "__main__":
    processor = get_data_processor()
    print(processor.process_data())
