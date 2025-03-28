MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# TAKING INPUT FROM THE USER

string_input = input('Please enter the string you want to convert to morse code: ').upper()

# INITIALIZING AN EMPTY LIST WHERE THE MORSE CODE WILL BE APPENDED

morse_code = []

# ITERATING OVER EVERY LETTER IN THE STRING AND THEN MATCHING IT WITH THE DICT ITEMS

for letter in string_input:
    if letter == ' ':
        morse_code.append(letter)
    for key, value in MORSE_CODE_DICT.items():
        if letter in key:
            morse_code.append(value)

# CONVERTING THE LIST TO A STRING

morse_code = ''.join(morse_code)
print(morse_code)