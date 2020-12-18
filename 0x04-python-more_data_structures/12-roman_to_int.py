#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    conversion = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman_string):
        if i > 0 and conversion[roman_string[i]] > conversion[roman_string[i - 1]]:
            result += conversion[roman_string[i]] - 2 * conversion[roman_string[i - 1]]
        else:
            result += conversion[roman_string[i]]
        i += 1
    return result
