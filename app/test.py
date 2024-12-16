import pytest
from app.main import fetch_data, fetch_with_retries, process_data, process_all_data, risky_api_call, unoptimized_loop, insecure_subprocess, hardcoded_password

def test_fetch_data():
    data = fetch_data(1)
    assert data == "data_1" or data is None  # Random failure rate

def test_fetch_with_retries():
    retries = 3
    data = fetch_with_retries(1, retries)
    assert data == "data_1" or data is None  # Test retry logic

def test_process_data():
    process_data("data_1", 1)
    assert 1 in user_data  # This can be problematic if the global variable is modified unexpectedly

def test_process_all_data():
    user_data = process_all_data()
    assert len(user_data) == 10

def test_risky_api_call():
    # Test risky API call (this is vulnerable to a variety of attacks)
    response = risky_api_call("malicious_input")
    assert "error" not in response  # Assumes that no errors occur

def test_unoptimized_loop():
    data = unoptimized_loop()
    assert len(data) == 1000000  # Inefficient, might cause memory issues on larger datasets

def test_insecure_subprocess():
    # This test is unsafe, as subprocess calls with unsanitized inputs can be exploited
    try:
        insecure_subprocess()
    except Exception:
        assert True  # Expecting an exception due to unsafe environment variable usage
import pytest
from app.main import DataProcessor, USER_DATA

# Mock DataProcessor class methods for unit tests
@pytest.fixture
def processor():
    return DataProcessor()

def test_fetch_data(processor):
    # Test the fetch_data method with a random failure rate
    data = processor.fetch_data(1)
    assert data == "data_1" or data is None  # 20% failure rate

def test_fetch_with_retries(processor):
    retries = 3
    # Test the retry logic
    data = processor.fetch_with_retries(1, retries)
    assert data == "data_1" or data is None  # Data should either be fetched or None

def test_process_data(processor):
    # Test process_data method
    processor.process_data("data_1", 1)  # Valid data should be processed
    assert USER_DATA[1] == "data_1"
    
    processor.process_data(None, 2)  # Invalid data should fail to process
    assert 2 not in USER_DATA  # User data should not contain the failed entry

def test_process_all_data(processor):
    # Test processing all data entries
    user_data = processor.process_all_data()
    assert len(user_data) == 10  # Should process 10 entries

    # Ensure first entry is processed or None based on fetch_data result
    assert user_data[0] == "data_0" or user_data[0] is None

def test_retry_logic(processor):
    # Test retry logic with multiple failures
    processor.fetch_data = lambda x: None  # Force failures
    data = processor.fetch_with_retries(1, retries=3)
    assert data is None  # Should still be None after all retries fail


def test_hardcoded_password():
    password = hardcoded_password()
    assert password == "mysecurepassword"  # This is insecure, should not be hardcoded
