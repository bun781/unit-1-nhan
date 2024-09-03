#my_lib.py
def check_input(msg:str, check:str) -> int:
    unsafe_data = msg
    safe = True
    for l in unsafe_data:
        if l not in check:
            safe = False

    if safe:
        output = int(unsafe_data)
    else:
        output = None
    return output

def add_letters(msg:str)->int:
    total = 0
    for letter in msg:
        total += ord(letter) - 96
    return total

def validation_bool(msg:str)->bool:
    unsafe_data = msg
    if unsafe_data in ['True', 'T', 't', '1', 'true']:
        output = True
    elif unsafe_data in ['False', 'F', 'f', '0', 'false']:
        output = False
    else:
        output = None
    return output

def mystery_box1(msg:str, lowered:bool):
    upper_to_lower = { #dictionary to turn uppercase into lowercase
        "A": "a",
        "B": "b",
        "C": "c",
        "D": "d",
        "E": "e",
        "F": "f",
        "G": "g",
        "H": "h",
        "I": "i",
        "J": "j",
        "K": "k",
        "L": "l",
        "M": "m",
        "N": "n",
        "O": "o",
        "P": "p",
        "Q": "q",
        "R": "r",
        "S": "s",
        "T": "t",
        "U": "u",
        "V": "v",
        "W": "w",
        "X": "x",
        "Y": "y",
        "Z": "z"
    }
    original_string = msg #orignal string
    lower = validation_bool(str(lowered)) #validate if the supposed boolean entered is a boolean
    new_string = '' #new string to output because python cant modify strings

    if lower: #if outside so only need to do if once
        for i in range(len(original_string)-1, -1, -1): #iterates string backwards
            if original_string[i] in upper_to_lower: #check if a letter is uppercase
                new_string += upper_to_lower[original_string[i]]
            else:
                new_string += original_string[i]
    else:
        for i in range(len(original_string)-1, -1, -1): #iterates string backwards
            new_string += original_string[i]

    return new_string

# mystery_box1("Hello", True)
# mystery_box1("Hello", False)

def mystery_box2(input_string:str):
    has_at = False #check if input_string is a valid email address
    for l in input_string:
        if l == '@':
            has_at = True

    user_name = '' #create string for username
    domain_name = '' #create string for domain name
    name_switched = False #check if loop has passed the @

    if not has_at: #will exit if email is not valid
        print('Not a valid email address, program exiting...')
        exit()
    else:
        for l in input_string:
            if not name_switched: #if not passed the @ yet, add the char to user_name
                if l == '@': #check if char is @
                    name_switched = True
                else: #else add char to username
                    user_name += l
            elif name_switched: #if passed username then just add the char directly to domain name
                domain_name += l

    #return output
    return user_name, domain_name
# print(mystery_box2("john.doe@gmail.com"))

def mystery_box3(a:int, b:int, c:int):
    if not check_input(str(a), '0123456789') or not check_input(str(b), '0123456789') or not check_input(str(c), '0123456789'):
        exit()
    if a < b:
        if a < c:
            smallest_possible_guess = a
        else:
            smallest_possible_guess = c
    elif b < c :
        smallest_possible_guess = b
    else:
        smallest_possible_guess = c

    biggest_possible_guess = a * b * c

    for i in range(smallest_possible_guess, biggest_possible_guess+1):
        if i % a == 0 and i % b == 0 and i % c == 0: #check if divisible by all
            return i
# print(mystery_box3(8, 6, 2))
# print(mystery_box3(18, 4, 7))
# print(mystery_box3(5, 10, 7))
# print(mystery_box3(5, 6, 3))

def mystery_box4(input_list:list):
    if not isinstance(input_list, list):
        print("Input lists only")
        exit()
    if len(input_list) < 7:
        print("Input list is too short")
        exit()
    for l in input_list:
        if str(l) not in '0123456789':
            print("Input positive integers only")
            exit()
    output_list = []
    total = 0
    for i in range(4):
        total += input_list[i]
        output_list.append(input_list[i])
    average = total / 5
    return average, output_list

print(mystery_box4([5, 6, 3, 8, 1, 7, 9]))









