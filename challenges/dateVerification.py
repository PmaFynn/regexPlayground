from main import test_regex
import re

"""
    https://callumacrae.github.io/regex-tuesday/challenge1.html

    This weeks Regex Tuesday challenge, the first challenge, is to make a regex which finds and highlights repeated words in a body of text. It is a fairly easy challenge, and future challenges will usually be trickier.

    You should just wrap the repeated word in a <strong> element. For example, this is is a test should be turned into this is <strong>is</strong> a test.

    To test a regular expression on the test cases below, type it into the text input. Each test case will be marked as passed or failed respectively - you are aiming to get as many test cases as you can to pass. Note that JavaScript must be enabled for this feature to work. The regex engine used is the JavaScript regex engine; it is similar to PCRE, but with a few differences.
"""

solution_pattern = r'\b(?=\d{4})(1[0-9]{3}|200[0-9]|201[0-2])\/(?!00)(0[1-9]|1[0-2])\/(?!00)([0-2][0-9]|3[01])\s([01][0-9]|2[0-3])\:[0-5][0-9](?:\:[0-5][0-9])?$'

# replacement = r'\1 <strong>\2</strong>'

test_cases = [
("2012/09/18 12:10", True),
("2001/09/30 23:59:11", True),
("1995/12/01 12:12:12", True),
("1001/01/07 14:27", True),
("2010/10/20 10:10", True),
("2000/01/01 01:01:01", True),
("2007/07/22 22:34:59", True),
("2010/05/05 00:00:00", True),
("2012/9/18 23:40", False),
("2013/09/09 09:09", False),
("2012/00/01 01:49:59", False),
("2012/13/25 22:17:00", False),
("1994/11/00 12:12", False),
("2012/12/4 12:12", False),
("2009/11/11 24:00:00", False),
("2012/06/24 13:60", False),
("2002/10/10 14:59:60", False),
("a2011/11/11 11:11:11", False),
("2005/05/05 05:05:05d", False),
]

def run_challenge():
    print("Date Matching Challenge")
    print("Source: https://callumacrae.github.io/regex-tuesday/challenge3.html")
    print("-----------------------------")
    print("Task: The third regex tuesday challenge is to match dates in YYYY/MM/DD HH:MM(:SS) format. YYYY should be a year between 1000 and 2012, and everything else should be a valid month, date, hour, minute and second. The seconds should be optional. Don't worry about leap years, and assume that all months have 30 days.\nTo test a regular expression on the test cases below, type it into the text input. Each test case will be marked as passed or failed respectively - you are aiming to get as many test cases as you can to pass. Note that JavaScript must be enabled for this feature to work. The regex engine used is the JavaScript regex engine; it is similar to PCRE, but with a few differences.")
    print("These are the Testcase:\n", test_cases)
    print("-----------------------------")
    print("\nDo you want to enter a regex?")
    
    while True:
        choice = input("[y]es | [n]o, see solution: ").lower()
        if choice in ['y', 'n']:
            break
        print("Please enter 'y' or 'n'")
    
    if choice == 'y':
        print("\nEnter your regex pattern:")
        user_pattern = input()
        print("\nTesting your pattern...")
        test_regex(user_pattern, test_cases)
    else:
        print("\nTesting solution pattern...")
        test_regex(solution_pattern, test_cases) 

if __name__ == "__main__":
    run_challenge()

