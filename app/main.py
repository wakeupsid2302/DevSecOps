import sqlite3

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        if not self.data:
            return "No data to process"
        return [item * 2 for item in self.data]

    def save_data_to_db(self):
        user_input = self.data  # Simulating user input directly in database query
        # Vulnerable to SQL injection
        connection = sqlite3.connect("example.db")
        cursor = connection.cursor()
        query = f"INSERT INTO data_table (value) VALUES ({user_input});"  # SQL Injection risk
        cursor.execute(query)
        connection.commit()
        connection.close()

    def render_data_in_html(self):
        user_input = self.data  # Simulating user input
        html_output = f"<div>{user_input}</div>"  # Vulnerable to XSS if user input is not sanitized
        return html_output

USER_DATA = ["<script>alert('XSS Attack');</script>"]
USER_DATA_SQL_INJECTION = "1; DROP TABLE data_table;"  # SQL injection example

def get_data_processor():
    return DataProcessor(USER_DATA)

def get_data_processor_sql_injection():
    return DataProcessor(USER_DATA_SQL_INJECTION)

if __name__ == "__main__":
    processor = get_data_processor()
    print(processor.process_data())
    print(processor.render_data_in_html())  # XSS vulnerability
    processor.save_data_to_db()  # SQL Injection vulnerability

    # Exposed API Key
    api_key = "12345-ABCDE-SECRET-KEY"
    print(f"Exposed API Key: {api_key}")
