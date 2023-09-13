#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (roman_string and isinstance(roman_string, str)):
        return 0

    num = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(roman_string)):
        if roman_string[i] in roman:
            if roman_string[i] == 'I':
                next_chindex = (i + 1) if i < (len(roman_string) - 1) else i
                n = 1 if roman_string[next_chindex] == 'I' else -1
                num += n
            else:
                num += roman[roman_string[i]]
        else:
            return 0
    return num
