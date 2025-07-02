
def intersection(foo: str, bar: str) -> str | None:
    result = None  # Default value if no overlapping characters are found
    if len(foo) > 0 and len(bar) > 0:  # Make sure both strings are not empty
        result = ""  # Initialize an empty string to hold shared characters
        for i in range(len(foo)):  # Go through each character in the first string
            current_character = foo[i]  # Get the current character
            if current_character in bar and current_character not in result:
                # If the character exists in both strings and isn't already added
                result += current_character  # Add it to the result
        if result == "":  # If nothing was added, return None
            result = None
    return result
def intersection(foo: str, bar: str) -> str | None:
    # ... your first function code here ...
    return result

def is_alphabetical(string: str) -> bool:
    result = True  # Start by assuming the string only contains letters
    if len(string) > 0:  # Make sure the string isn’t empty
        for i in range(len(string)):  # Check every character one by one
            current_character = string[i]
            ascii_value = ord(current_character)  # Convert the character to its ASCII number

            # If the character is not in the uppercase (A–Z) or lowercase (a–z) ASCII range:
            if not ((ord('A') <= ascii_value <= ord('Z')) or
                    (ord('a') <= ascii_value <= ord('z'))):
                result = False  # Found a non-letter character, so mark result as False
    return result
def letters_only(string: str) -> str | None:
    result = None  # Default to None in case we find no letters at all
    if len(string) > 0:  # Only continue if the input isn't empty
        result = ""  # Start an empty string to collect valid characters
        for i in range(len(string)):  # Go through each character in the string
            current_character = string[i]
            ascii_value = ord(current_character)  # Get the ASCII value of the character

            # Check if character is a letter (either uppercase A–Z or lowercase a–z)
            if ((ord('A') <= ascii_value <= ord('Z')) or
                (ord('a') <= ascii_value <= ord('z'))):
                result += current_character  # Add the valid letter to the result string

        if result == "":  # If result is still empty after checking all characters
            result = None  # Set to None to match function requirement
    return result
def generate_palindrome(string: str) -> str | None:
    result = None  # Set default return value to None in case input is empty
    if len(string) > 0:  # Only proceed if the input string has characters
        reverse = ""  # This will hold the reversed version of the string
        for i in range(len(string) - 1, -1, -1):  
            # Loop backwards from last character to first
            reverse += string[i]  # Add each character from the end to the beginning
        result = string + reverse  # Combine original string with its reversed copy
    return result
def is_palindrome(string: str) -> bool:
    result = False  # Default to False unless proven otherwise
    only_letters = ""  # Create a cleaned version of the string with only letters

    for ch in string:
        # Include the character if it's a letter
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            only_letters += ch.lower()  # Add the lowercase version

    reversed_letters = ""  # Prepare the reversed string
    for i in range(len(only_letters) - 1, -1, -1):
        reversed_letters += only_letters[i]

    if only_letters == reversed_letters:  # Check if cleaned string equals its reverse
        result = True

    return result

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
