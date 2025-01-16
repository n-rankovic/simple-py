# Code with issues

import os  # Unused import (Code Smell)

def authenticate(user, password):
    hardcoded_password = "123456"  # Hardcoded sensitive information (Security Issue)
    if password == hardcoded_password:
        print(f"Welcome, {user}!")  # Use of print instead of logging (Code Smell)

def calculate_total(items):
    total = 0
    for i in range(len(items)):  # Inefficient iteration (Code Smell)
        total += items[i]
    return total

def read_file(filename):
    with open(filename, 'r') as file:  # Missing error handling for file operations (Code Smell)
        data = file.read()
    return data

def vulnerable_query(user_input):
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # SQL Injection (Security Issue)
    print(query)

# Main code
print(authenticate("admin", "123456"))  # No return value handled (Bug)
print(calculate_total([1, 2, 3]))  # Inefficient loop
read_file("/etc/passwd")  # Security risk: sensitive file access
vulnerable_query("admin'; DROP TABLE users; --")  # SQL Injection
