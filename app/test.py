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

def test_hardcoded_password():
    password = hardcoded_password()
    assert password == "mysecurepassword"  # This is insecure, should not be hardcoded
