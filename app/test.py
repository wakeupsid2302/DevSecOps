# app/test.py
import sys
import os
from pathlib import Path

# Add the app directory to the Python path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'app'))

import pytest
from main import f1, f2, f3, f4, fetch_data, user_data

def test_f1():
    f1()
    assert len(user_data) == 10

def test_f2():
    f2()
    assert user_data[5] == "data_5"
