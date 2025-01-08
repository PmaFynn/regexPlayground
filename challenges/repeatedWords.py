from main import test_regex
import re

"""
    https://callumacrae.github.io/regex-tuesday/challenge1.html

    This weeks Regex Tuesday challenge, the first challenge, is to make a regex which finds and highlights repeated words in a body of text. It is a fairly easy challenge, and future challenges will usually be trickier.

    You should just wrap the repeated word in a <strong> element. For example, this is is a test should be turned into this is <strong>is</strong> a test.

    To test a regular expression on the test cases below, type it into the text input. Each test case will be marked as passed or failed respectively - you are aiming to get as many test cases as you can to pass. Note that JavaScript must be enabled for this feature to work. The regex engine used is the JavaScript regex engine; it is similar to PCRE, but with a few differences.
"""

solution_pattern = r'(\b[^\s]+\b)\s(\1\b)'

replacement = r'\1 <strong>\2</strong>'

test_cases = [
    ("This is a test", "This is a test"),
    ("This is is a test", "This is <strong>is</strong> a test"),
    ("This test test is is", "This test <strong>test</strong> is <strong>is</strong>"),
    ("This test is a test", "This test is a test"),
    ("This this test is a test", "This <strong>this</strong> test is a test"),
    ("cat dog dog cat dog", "cat dog <strong>dog</strong> cat dog"),
    ("This test is a test tester", "This test is a test tester"),
    ("hello world hello world", "hello world hello world"),
    ("This nottest test is something", "This nottest test is something"),
    ("This is IS a test", "This is <strong>IS</strong> a test"),
    ("<Mack> I'll I'll be be back back in in a a bit bit.", "<Mack> I'll <strong>I'll</strong> be <strong>be</strong> back <strong>back</strong> in <strong>in</strong> a <strong>a</strong> bit <strong>bit</strong>."),
]

def run_challenge():
    print("Repeating Words Challenge")
    print("Source: https://callumacrae.github.io/regex-tuesday/challenge1.html")
    print("-----------------------------")
    print("Task: This weeks Regex Tuesday challenge, the first challenge, is to make a regex which finds and highlights repeated words in a body of text. It is a fairly easy challenge, and future challenges will usually be trickier.\n\nYou should just wrap the repeated word in a <strong> element. For example, this is is a test should be turned into this is <strong>is</strong> a test.\n\nTo test a regular expression on the test cases below, type it into the text input. Each test case will be marked as passed or failed respectively - you are aiming to get as many test cases as you can to pass. Note that JavaScript must be enabled for this feature to work. The regex engine used is the JavaScript regex engine; it is similar to PCRE, but with a few differences.\n")
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
        test_regex(solution_pattern, test_cases, replacement, flags=re.IGNORECASE)

if __name__ == "__main__":
    run_challenge()
