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

