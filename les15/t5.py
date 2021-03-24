def roman_to_int(roman):
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic = 0
    for i in range(len(roman)):
        if i > 0 and rom_dic[roman[i]] > rom_dic[roman[i-1]]:
            arabic += rom_dic[roman[i]] - (2 * rom_dic[roman[i-1]])
        else:
            arabic += rom_dic[roman[i]]

    return arabic


print(roman_to_int('XIX'))
print(roman_to_int('XCIV'))
print(roman_to_int('IV'))
print(roman_to_int('V'))
