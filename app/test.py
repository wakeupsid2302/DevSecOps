import pytest
from app.main import DataProcessor, USER_DATA, USER_DATA_SQL_INJECTION

def test_process_data():
    processor = DataProcessor(USER_DATA)
    result = processor.process_data()
    assert result == [2, 4, 6], "Data should be doubled"

def test_save_data_to_db_sql_injection():
    # Test to see if SQL injection can occur
    processor = DataProcessor(USER_DATA_SQL_INJECTION)
    with pytest.raises(Exception):
        processor.save_data_to_db()  # This should fail or cause an error in case of SQL injection

def test_render_data_in_html_xss():
    processor = DataProcessor(["<script>alert('XSS Attack');</script>"])
    rendered_html = processor.render_data_in_html()
    # Check that the XSS attempt is part of the output
    assert "<script>" in rendered_html, "XSS vulnerability found!"
