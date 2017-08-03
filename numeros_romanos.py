'''
Converter algorismos romanos em indo-arabicos.
Converter algorismos indo-arabicos em romanos.
'''

def read_roman_into_arabic(number,letters,numbers):
    output = 0
    prev_value = 0
    for index,digit in enumerate(reversed(number)):
        value = numbers[letters.index(digit)]
        if index > 0:
            if value >= prev_value:
                output += value
            else:
                output -= value
        else:
            output += value
        prev_value = value
    return output

def read_arabic_into_roman(number,letters,numbers):
    output = ""
    for index, value in enumerate(numbers):
        letter = letters[index]
        count = 0
        while number >= value:
            output += letter
            count += 1
            #print(number,value,output)
            if count > 3:
                output = output[:-4]
                if (output and output[-1] in ("D","L","V")):
                    output = output[:-1]
                    output += letters[index] + letters[index - 2]
                else:
                    output += letters[index]+letters[index-1]
            number -= value
    return output

def roman_converter(number):
    letters = ("M","D","C","L","X","V","I")
    numbers = (1000, 500, 100, 50, 10, 5, 1)
    if type(number) == str:
        return read_roman_into_arabic(number,letters,numbers)
    if type(number) == int:
        return read_arabic_into_roman(number, letters, numbers)
    return


assert roman_converter('I') == 1
assert roman_converter('II') == 2
assert roman_converter('III') == 3
assert roman_converter('IV') == 4
assert roman_converter('V') == 5
assert roman_converter('VI') == 6
assert roman_converter('DCL') == 650
assert roman_converter('CMIX') == 909
assert roman_converter(1) == 'I'
assert roman_converter(2) == 'II'
assert roman_converter(3) == 'III'
assert roman_converter(4) == "IV"
assert roman_converter(5) == 'V'
assert roman_converter(7) == "VII"
assert roman_converter(9) == "IX"
assert roman_converter(90) == "XC"
assert roman_converter(140) == "CXL"
assert roman_converter(149) == "CXLIX"
assert roman_converter(94) == "XCIV"
assert roman_converter(40) == "XL"
# assert roman_converter(10) == "X"
# assert roman_converter(50) == "L"
# assert roman_converter(150) == "DL"
# assert roman_converter(1150) == "MDL"
