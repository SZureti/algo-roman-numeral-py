# convert my JavaScript solution to Python

def to_roman_lazy(num):
    # create container
    output = ""
    # Add/list pairs roman to arabic
    roman_numeral_to_arabic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    # create descending priority order
    roman_numeral_priority_order = ["M", "D", "C", "L", "X", "V", "I"]

    for roman_numeral in roman_numeral_priority_order:
        arabic_value = roman_numeral_to_arabic[roman_numeral]
        
        # // is integer division (automatically does what Math.floor does)
        count = num // arabic_value
        
        # multiply a string by an integer to repeat it
        output += roman_numeral * count
        
        num -= arabic_value * count
        
    return output


def to_roman(num):
    output = ""
    
    # Added the subtractive pairs
    roman_numeral_to_arabic = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    roman_numeral_priority_order = [
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
    ]
    
    # iterate over the list 
    for current_roman in roman_numeral_priority_order:
        current_value = roman_numeral_to_arabic[current_roman]

        # Find how many times the value fit
        count = num // current_value
        
        # Append the string
        output += current_roman * count

        # Subtract the value
        num -= (count * current_value)
        
        # If number is reduced to zero, stop 
        if num == 0:
            break
            
    return output

# --- Testing the functions ---
print(to_roman_lazy(4))  # Output: IIII
print(to_roman(4))       # Output: IV
print(to_roman(944))     # Output: CMXLIV
print(to_roman(1111))    # Output: MCXI
print(to_roman_lazy(6))  # Output: VI
