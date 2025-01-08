from main import test_regex
import re

"""
    Should match whole line
"""
regex_pattern = r'\d+\s\-\s\d+\s\=\s(?:\-\s)?\d+'

#replacement = r'\1 <strong>\2</strong>'

test_cases = [
"12 - 12 = 0",
"56 - 56 = 0",
"0 - 0 = 0",
"0 - 13 = - 13",
"25 - 0 = 25",
]

test_regex(regex_pattern, test_cases)
