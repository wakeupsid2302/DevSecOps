# app/test.py
import pytest
from app.main import DataProcessor, USER_DATA

def test_process_data():
    processor = DataProcessor(USER_DATA)
    result = processor.process_data()
    assert result == [2, 4, 6], "Data should be doubled"

def test_no_data():
    processor = DataProcessor([])
    result = processor.process_data()
    assert result == "No data to process", "Empty data should return a no-data message"
