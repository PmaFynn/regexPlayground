from main import test_regex

# Fixed pattern: removed square brackets and unnecessary word boundary
regex_pattern = r'(\b\w+\b)\s+\1\b'

# Fixed replacement: using \1 instead of $1
replacement = r'\1 <strong>\1</strong>'

test_cases = [
    ("This is a test", "This is a test"),
    ("This is is a test", "This is <strong>is</strong> a test"),
]

test_regex(regex_pattern, test_cases, replacement)
