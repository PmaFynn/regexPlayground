from main import test_regex
import re

# Fixed pattern: removed square brackets and unnecessary word boundary
regex_pattern = r'(\b[^\s]+\b)\s(\1\b)'

# Fixed replacement: using \1 instead of $1
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

test_regex(regex_pattern, test_cases, replacement, flags=re.IGNORECASE)
