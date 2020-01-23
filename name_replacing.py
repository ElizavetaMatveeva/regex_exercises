# Task: to protect people's privacy, replace their last names with just the initial

import re


def hide_names(text):
    pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([A-Z])[a-z]+')
    return pattern.sub("\g<1> \g<2>", text)


print(hide_names("Last night Mrs. Daisy and Mr. White stole Ms. Chow's jewelry"))
# Last night Mrs. D and Mr. W stole Ms. C's jewelry
