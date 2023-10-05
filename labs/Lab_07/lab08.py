"""
Lab 7 | CS211 Winter 2023
Name: Joshua I.
Google Pythex for helping with regular expressions
"""

import re
import math


def validate_email(email: str) -> bool:
    regex = re.fullmatch("^[A-Za-z][A-Za-z0-9]+ @[A-Za-z0-9]+\.(com|edu)")
    return regex

def validate_pass(password: str):
    regex = re.fullmatch("(?=.*\d)(?=.*\W).{10,}", password)
    return regex

if __name__ == "__main__":
    email = input("provide and email address: ")

    while not validate_email(email):
        input("Invalaid email...Try again")

    while not validate_email(email):
        input("Invalaid pass...Try again")

    
