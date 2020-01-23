# Task: extract phone number from a string,
# make sure it's a separately written number, not buried between random symbols

import re


def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


print(extract_phone("call me at 469 531-9227"))  # '469 531-9227'
print(extract_phone("call me at 414 754-032455gfd"))  # None
