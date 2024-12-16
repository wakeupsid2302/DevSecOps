import pytest
from app.main import DataProcessor, USER_DATA

@pytest.fixture
def processor():
    return DataProcessor()

def test_fetch_data(processor):
    data = processor.fetch_data(1)
    assert data == "data_1" or data is None  # Test fetch data function with a 20% chance of failure

def test_fetch_with_retries(processor):
    retries = 3
    data = processor.fetch_with_retries(1, retries)
    assert data == "data_1" or data is None  # Test retry logic

def test_process_data(processor):
    # Test the process_data function
    processor.process_data("data_1", 1)  # Valid data should be processed
    processor.process_data(None, 2)  # Invalid data should fail to process
    assert processor.user_data[1] == "data_1"
    assert 2 not in processor.user_data

def test_process_all_data(processor):
    user_data = processor.process_all_data()
    assert len(user_data) == 10  # Should process 10 entries
    assert user_data[0] == "data_0" or user_data[0] is None  # Check for valid data or None
