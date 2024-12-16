# tests/test_main.py

import pytest
from app.main import f1, f2, f3, f4, fetch_data, user_data

def test_f1():
    f1()
    assert user_data[0] == "mock_data_0"
    assert len(user_data) == 10

def test_f2():
    f2()
    assert user_data[5] == "mock_data_5"

# Add more tests as needed
