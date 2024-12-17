# app/test.py
import pytest
from app.main import DataProcessor, USER_DATA, DataProcessorDuplicate, USER_DATA_DUPLICATE

def test_process_data():
    processor = DataProcessor(USER_DATA)
    result = processor.process_data()
    assert result == [2, 4, 6], "Data should be doubled"

def test_no_data():
    processor = DataProcessor([])
    result = processor.process_data()
    assert result == "No data to process", "Empty data should return a no-data message"

# Duplicated test case for the duplicated code
def test_process_data_duplicate():
    processor = DataProcessorDuplicate(USER_DATA_DUPLICATE)
    result = processor.process_data_duplicate()
    assert result == [2, 4, 6], "Data should be doubled (duplicate)"

def test_no_data_duplicate():
    processor = DataProcessorDuplicate([])
    result = processor.process_data_duplicate()
    assert result == "No data to process", "Empty data should return a no-data message (duplicate)"

# Further duplication in tests
def test_process_data_duplicate_2():
    processor = DataProcessorDuplicate(USER_DATA_DUPLICATE)
    result = processor.process_data_duplicate()
    assert result == [2, 4, 6], "Data should be doubled (duplicate 2)"

def test_no_data_duplicate_2():
    processor = DataProcessorDuplicate([])
    result = processor.process_data_duplicate()
    assert result == "No data to process", "Empty data should return a no-data message (duplicate 2)"
