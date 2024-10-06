# utils.py

import logging

logging.basicConfig(level=logging.ERROR, filename='app.log')

def validate_email(email):
    # Basic email validation logic (could use regex for better validation)
    return "@" in email and "." in email

def validate_password(password):
    return len(password) >= 8  # Simple password length check

def log_error(message):
    logging.error(message)
