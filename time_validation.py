# Task: check if a string is formatted correctly as a time

import re


def is_valid_time(string):
    time_pattern = re.compile(r'^\d{1,2}:\d{2}$')
    time = time_pattern.search(string)
    if time:
        return True
    return False


print(is_valid_time("20:12"))  # True
print(is_valid_time("2003"))  # False
print(is_valid_time("1:34"))  # True
