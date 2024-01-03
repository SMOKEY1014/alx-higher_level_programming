#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from the ASCII value
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(char), end='')

    # Print a new line after processing the entire string
    print()
