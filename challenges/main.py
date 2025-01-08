import re
from typing import List, Union, Tuple

def test_regex(
    pattern: str,
    test_cases: List[Union[str, Tuple[str, str]]],
    replacement: str = None
):
    """
    Test a regex pattern against multiple strings and print the results.
    Can also test replacements against expected outcomes.
    
    Args:
        pattern (str): The regex pattern to test
        test_cases (List): Can be either:
            - List of strings to test against
            - List of tuples (test_string, expected_replacement)
        replacement (str, optional): Replacement pattern to use with re.sub
    """
    print(f"\nTesting pattern: {pattern}")
    if replacement:
        print(f"Replacement: {replacement}")
    print("-" * 50)
    
    compiled_pattern = re.compile(pattern)
    
    for test_case in test_cases:
        # Handle both simple strings and tuple test cases
        if isinstance(test_case, tuple):
            test_str, expected_replacement = test_case
        else:
            test_str = test_case
            expected_replacement = None
            
        print(f"\nString: '{test_str}'")
        
        # Test if there's a match
        match = compiled_pattern.search(test_str)
        if match:
            print("✓ Match found!")
            
            # Find all matches
            matches = compiled_pattern.findall(test_str)
            if matches:
                print(f"Found matches: {matches}")
            
            # Show groups if any
            if match.groups():
                print(f"Groups: {match.groups()}")
        # Perform replacement if replacement pattern provided
        if replacement:
            replaced_text = compiled_pattern.sub(replacement, test_str)
            print(f"Replaced text: '{replaced_text}'")
            
            # Compare with expected replacement if provided
            if expected_replacement:
                if replaced_text == expected_replacement:
                    if match:
                        print(f"✓ Matches expected replacement")
                    else:
                        print("✓ No match found. As intended!")
                        print(f"✓ Matches expected replacement")
                else:
                    print("✗ No match")
                    print(f"✗ Expected: '{expected_replacement}'")

# Example usage
if __name__ == "__main__":
    # Example: Phone number formatting
    phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
    phone_tests = [
        ("Call me at 123-456-7890 today", "Call me at (123) 456-7890 today"),
        ("Multiple: 123-456-7890 and 987-654-3210", "Multiple: (123) 456-7890 and (987) 654-3210"),
        "No phone here",  # No expected replacement
    ]
    replacement_pattern = r'(\1) \2-\3'
    test_regex(phone_pattern, phone_tests, replacement_pattern)
