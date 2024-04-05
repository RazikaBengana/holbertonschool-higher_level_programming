#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rom_num = 0

    for j in range(len(roman_string)):

        if j > 0 and roman[roman_string[j]] > roman[roman_string[j - 1]]:
            rom_num += roman[roman_string[j]] - 2 * \
                        roman[roman_string[j - 1]]

        else:
            rom_num += roman[roman_string[j]]

    return rom_num
