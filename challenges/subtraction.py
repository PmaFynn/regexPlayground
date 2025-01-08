from main import test_regex
import re

"""
    Should match whole line
"""
solution_pattern = r'\d+\s\-\s\d+\s\=\s(?:\-\s)?\d+'

#replacement = r'\1 <strong>\2</strong>'

test_cases = [
"12 - 12 = 0",
"56 - 56 = 0",
"0 - 0 = 0",
"0 - 13 = - 13",
"25 - 0 = 25",
]

def run_challenge():
    print("Subtraction Challenge")
    print("-----------------------------")
    print("Task: Should match whole line")
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
        test_regex(user_pattern, test_cases, replacement)
    else:
        print("\nTesting solution pattern...")
        test_regex(solution_pattern, test_cases, flags=re.IGNORECASE)

if __name__ == "__main__":
    run_challenge()
