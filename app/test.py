import pytest
from app.main import DataProcessor, USER_DATA, DataProcessorDuplicate, USER_DATA_DUPLICATE

def test_process_data():
    processor = DataProcessor([1, 2, 3])  # Corrected test data to integers
    result = processor.process_data()
    assert result == [2, 4, 6], "Data should be doubled"

def test_no_data():
    processor = DataProcessor([])
    result = processor.process_data()
    assert result == "No data to process", "Empty data should return a no-data message"

# Duplicated test case for the duplicated code
def test_process_data_duplicate():
    processor = DataProcessorDuplicate([1, 2, 3])  # Corrected test data to integers
    result = processor.process_data_duplicate()
    # XSS vulnerability: Testing for XSS payload in response
    assert result == [
        "<script>alert('XSS Attack');</script>1", 
        "<script>alert('XSS Attack');</script>2", 
        "<script>alert('XSS Attack');</script>3"
    ], "Data should contain XSS payload (duplicate)"

def test_no_data_duplicate():
    processor = DataProcessorDuplicate([])
    result = processor.process_data_duplicate()
    assert result == "No data to process", "Empty data should return a no-data message (duplicate)"

# Further duplication in tests
def test_process_data_duplicate_2():
    processor = DataProcessorDuplicate([1, 2, 3])  # Corrected test data to integers
    result = processor.process_data_duplicate()
    # XSS vulnerability: Testing for XSS payload in response
    assert result == [
        "<script>alert('XSS Attack');</script>1", 
        "<script>alert('XSS Attack');</script>2", 
        "<script>alert('XSS Attack');</script>3"
    ], "Data should contain XSS payload (duplicate 2)"

def test_no_data_duplicate_2():
    processor = DataProcessorDuplicate([])
    result = processor.process_data_duplicate()
    assert result == "No data to process", "Empty data should return a no-data message (duplicate 2)"
