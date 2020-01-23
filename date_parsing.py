# Task: check if a string matches one of the following date formats:
# "dd/mm/yyyy", "dd.mm.yyyy", "dd,mm,yyyy"
# Return a dictionary containing the three parts of the date with the keys "d", "m", and "y"

import re


def parse_date(data):
    date_pattern = re.compile(r"""^(?P<day>\d{2})   # Day group
                                  [/.,]             # Delimiter
                                  (?P<month>\d{2})  # Month group
                                  [/.,]             # Delimiter
                                  (?P<year>\d{4})$  # Year group""", re.VERBOSE)
    match = date_pattern.search(data)
    if match:
        return {'d': match.group('day'), 'm': match.group('month'), 'y': match.group('year')}
    return None


print(parse_date("22.01.1995"))  # {'d': '22', 'm': '01', 'y': '1995'}
print(parse_date("02/04/2020"))  # {'d': '02', 'm': '04', 'y': '2020'}
print(parse_date("4-12-2009"))  # None
print(parse_date("fd31/03/1946"))  # None
