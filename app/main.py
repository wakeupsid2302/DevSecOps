# app/main.py
import os

def hello_world():
    secret = os.getenv("SECRET_API_KEY", "default_secret")  # Demonstrates a secret pattern
    print(f"Hello, World! Using secret: {secret}")

if __name__ == "__main__":
    hello_world()
