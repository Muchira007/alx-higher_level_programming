#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {}
    key_list = []
    total = 0
    i = 0

    roman_dict['I'] = 1
    roman_dict['IV'] = 4
    roman_dict['IX'] = 9
    roman_dict['V'] = 5
    roman_dict['X'] = 10
    roman_dict['XL'] = 40
    roman_dict['L'] = 50
    roman_dict['XC'] = 90
    roman_dict['C'] = 100
    roman_dict['CD'] = 400
    roman_dict['D'] = 500
    roman_dict['CM'] = 900
    roman_dict['M'] = 1000

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    while i < len(roman_string):
        if i < len(roman_string) - 1 and roman_string[i:i+2] in roman_dict:
            total += roman_dict[roman_string[i:i+2]]
            i += 2
        else:
            total += roman_dict[roman_string[i]]
            i += 1

    return total
