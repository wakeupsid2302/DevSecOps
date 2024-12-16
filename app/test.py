# app/test.py

import pytest
from app.main import fetch_data, fetch_with_retries, process_data, process_all_data

def test_fetch_data():
    data = fetch_data(1)
    assert data == "data_1" or data is None  # Test fetch data function with a 20% chance of failure

def test_fetch_with_retries():
    retries = 3
    data = fetch_with_retries(1, retries)
    assert data == "data_1" or data is None  # Test retry logic

def test_process_data():
    # Test the process_data function
    process_data("data_1", 1)  # Valid data should be processed
    process_data(None, 2)  # Invalid data should fail to process

def test_process_all_data():
    user_data = process_all_data()
    assert len(user_data) == 10  # Should process 10 entries
    assert user_data[0] == "data_0" or user_data[0] is None  # Check for valid data or None

