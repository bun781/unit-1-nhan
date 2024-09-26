#sha1265 library is for hashing the access code so it can be stored securely
from hashlib import sha256

#function to validate inputa
def valid(string:str, validation:str):
    valid = True
    for letter in string:
        if letter not in validation: #loop through each character to see if they are valid (in validation string) or not
            valid = False
            break
    return valid
def input_num_in_range(start_text:str,error_text:str,lowest_option:int,highest_option:int):
    accepted = False
    a = start_text
    while not accepted:
        option_str = input(a)
        a = error_text
        if not valid(option_str, '0123456789'):
            continue

        option = int(option_str)

        if option < lowest_option or option > highest_option:
            text = error_text
        else:
            accepted = True
    return option

#function for encryption
def generate_key_from_string(input_string:str):
    value_string = "1234567890-=~!@#$%^&*()_+qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
    letter_product = 1
    for letter in input_string:
        letter_product *= (value_string.index(letter) + 1) #+1 to make sure no number is 0
    string_letter_product = str(letter_product)
    key_string = ''
    if len(string_letter_product) < 4:
        while len(string_letter_product) < 4:
            string_letter_product += "0"
        key_string += string_letter_product
    elif len(string_letter_product) > 4:
        key_string += string_letter_product[0:4] #get the first 4 values
    else: #when len(string_letter_product) = 4
        key_string += string_letter_product
    return key_string
def base_10_to_2_15_bits(base_10_number:int):
    base_2_number_string = ''
    if base_10_number == 0:
        base_2_number_string = '0'
    base_10_number = int(base_10_number)
    while base_10_number > 0:
        remainder = base_10_number % 2
        base_2_number_string = str(remainder) + base_2_number_string
        base_10_number = base_10_number // 2 #floor division to make sure number is always correct

    while len(base_2_number_string) < 15:
        base_2_number_string = "0" + base_2_number_string

    return base_2_number_string
def encrypt(original:int, key:int):
    binary_original = base_10_to_2_15_bits(original) #change into 15bit binary string (as 9999 is 14 bit, so +1 because 15 is more flexible)
    binary_key = base_10_to_2_15_bits(key)

    round_1 = ''
    for i in range(15): #xor orignal and key
        if binary_original[i] == binary_key[i]:
            round_1 += '0'
        else:
            round_1 += '1'

    round_2 = []
    divided_key = []
    for i in range(0,15,5): #split into 3 parts
        round_2.append(round_1[i:i+5])
        divided_key.append(binary_key[i:i+5])
    shift = key % 3
    new_round_2 = round_2[shift:] + round_2[:shift] #shift the order of the partitions for the original string
    round_3 = ['','','']
    for i in range(3):
        for j in range(5):
            if new_round_2[i][j] == divided_key[i][j]: #xor partition of original string with the corresponding partition of the key
                round_3[i] += '1'
            else:
                round_3[i] += '0'
    round_4 =''
    for let in round_3:
        round_4 += let
    round_5 = int(round_4, 2) #turn the binary string back into integer
    return round_5
def decrypt(encrypted:int, key:int):
    binary_encrypted = base_10_to_2_15_bits(encrypted)
    binary_key = base_10_to_2_15_bits(key)

    divided_binary_encrypted = []
    divided_binary_key = []
    for i in range(0,15,5):
        divided_binary_encrypted.append(binary_encrypted[i:i+5])
        divided_binary_key.append(binary_key[i:i+5])


    divided_binary_encrypted_1 = ['','','']
    for i in range(3):
        for j in range(5):
            if divided_binary_encrypted[i][j] == divided_binary_key[i][j]:
                divided_binary_encrypted_1[i] += '1'
            else:
                divided_binary_encrypted_1[i] += '0'

    shift = key % 3
    new_divided_binary_encrypted_1 = divided_binary_encrypted_1[(3-shift):] + divided_binary_encrypted_1[:(3-shift)]
    original = ''
    for i in range(3):
        for j in range(5):
            if new_divided_binary_encrypted_1[i][j] == divided_binary_key[i][j]:
                original += '0'
            else:
                original += '1'
    return int(original, 2)

#function that returns a colored string
def console_text(message:str,color:str):
    end = "\033[00m"    #stop further message from accidentally being color
    return f"{color}{message}{end}" #return the colored message as f string

#function for normal mode
def menu():
    for i in range(200): #as window
        print("\n")
    print('''
 /$$   /$$                               /$$                                                   /$$$$$$$  /$$ /$$                          
| $$  /$$/                              |__/                                                  | $$__  $$|__/| $$                          
| $$ /$$/   /$$$$$$   /$$$$$$  /$$   /$$ /$$ /$$$$$$$$  /$$$$$$  /$$  /$$  /$$  /$$$$$$       | $$  \ $$ /$$| $$   /$$  /$$$$$$   /$$$$$$$
| $$$$$/   |____  $$ /$$__  $$| $$  | $$| $$|____ /$$/ |____  $$| $$ | $$ | $$ |____  $$      | $$$$$$$ | $$| $$  /$$/ /$$__  $$ /$$_____/
| $$  $$    /$$$$$$$| $$  \__/| $$  | $$| $$   /$$$$/   /$$$$$$$| $$ | $$ | $$  /$$$$$$$      | $$__  $$| $$| $$$$$$/ | $$$$$$$$|  $$$$$$ 
| $$\  $$  /$$__  $$| $$      | $$  | $$| $$  /$$__/   /$$__  $$| $$ | $$ | $$ /$$__  $$      | $$  \ $$| $$| $$_  $$ | $$_____/ \____  $$
| $$ \  $$|  $$$$$$$| $$      |  $$$$$$/| $$ /$$$$$$$$|  $$$$$$$|  $$$$$/$$$$/|  $$$$$$$      | $$$$$$$/| $$| $$ \  $$|  $$$$$$$ /$$$$$$$/
|__/  \__/ \_______/|__/       \______/ |__/|________/ \_______/ \_____/\___/  \_______/      |_______/ |__/|__/  \__/ \_______/|_______/ 
 
 /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/                                                                                                               
    ''')
    print('''
   ___ ___  _  _ ___  ___  _    ___     _  _ ___ ___ _____ ___  _____   __  _ 
  / __/ _ \| \| / __|/ _ \| |  | __|   | || |_ _/ __|_   _/ _ \| _ \ \ / / (_)
 | (_| (_) | .` \__ \ (_) | |__| _|    | __ || |\__ \ | || (_) |   /\ V /   _ 
  \___\___/|_|\_|___/\___/|____|___|   |_||_|___|___/ |_| \___/|_|_\ |_|   (_)
                                                                                                                            
    ''')
def load_passcode_hashed():
    with open('access_code.txt', mode='r') as file:
        passcode_hashed = file.readlines()[0]
    return passcode_hashed
def bike_input_check_secret_entered(bike_price_data, available_bike_data, passcode_hashed):
    accepted = False
    text = f"Welcome to Karuizawa Rentals, please check the rental rate per hour by entering a valid bike number. To check for available bikes, enter X, type ""clear"" to clear the console history"
    color = "\33[0;35m"
    while not accepted:
        bike_num_str = input(console_text(f'[{text}]:', color))  # ask for input
        if sha256(bike_num_str.encode('utf-8')).hexdigest() == passcode_hashed: #the string is the sha265 hashed version of the passcode_dictionary(for security reasons)
            return True
        elif bike_num_str in 'xX':
            string_available_bike_data = ''
            for num, bike in enumerate(available_bike_data):
                if num % 20 == 19: #make 20 columns
                    string_available_bike_data += f"{bike},\n"
                else:
                    string_available_bike_data += f"{bike}, "
            print(console_text("The available bikes are: ", "\33[0;32m"))
            print(console_text(string_available_bike_data, "\33[0;36m"))
            print(console_text("Above are the available bikes.", "\33[0;32m")) #make long list more visible for smaller displays
            print('-----------------------')
            print()
            continue
        elif bike_num_str == 'clear':
            menu()
            text = 'Welcome to Karuizawa Rentals, please check the rental rate per hour by entering a valid bike number. To check for available bikes, enter X, type ""clear"" to clear the console history'
            continue
        elif not valid(bike_num_str, '0123456789'): #check if input is number
            text = f"Please enter a valid bike number, please try again"
            color = "\33[0;33m"
            continue  #go back to asking for input

        elif f'{bike_num_str:02}' not in available_bike_data: #check if number is valid
            text = f"Please enter a valid bike number, please try again"
            color = "\33[0;33m"
            continue #go back to asking for input
        else:
            bike_num = int(bike_num_str)
            accepted = True #end the loop
    print(console_text(f'\nYou can rent bike {bike_num:02} for ¥{bike_price_data[f"{bike_num:02}"]}/hour',"\33[0;32m"))  # bike_price_data[f"{bike_num:02} returns the price from the dictionary. Not made a variable to save memory.
    print("-------------")  # for clarity #print the bike rental rate
    print()

#functions for loading bike price data
def load_bike_raw_data():
    with open('bike_data.csv', mode ='r') as f:
        bike_data_raw = f.readlines()
    return bike_data_raw
def load_bike_price_data_data(bike_data_raw):
    bike_price_data = {}
    for item in bike_data_raw: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',')

        #unpacking
        name = data_separated[0]
        price = data_separated[1]

        #add to bike_data (a dictionary)
        bike_price_data[name] = int(price)
    return bike_price_data
def load_bike_availability_data(bike_data_raw):
    available_bike_data = []
    for item in bike_data_raw: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',') #split the data into separate bike number and price
        available_bike_data.append(data_separated[0]) #add the bike number to the availability list
    return available_bike_data

#function for passcode manager
def secret_menu():
    for i in range(200): #as window
        print("\n")
    print('''
 /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$       /$$      /$$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$| $$_____/      | $$$    /$$$ /$$__  $$| $$$ | $$ /$$__  $$ /$$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$| $$  \__/| $$  \__/| $$  \__/| $$  \ $$| $$  \ $$| $$            | $$$$  /$$$$| $$  \ $$| $$$$| $$| $$  \ $$| $$  \__/| $$      | $$  \ $$
| $$$$$$$/| $$$$$$$$|  $$$$$$ |  $$$$$$ | $$      | $$  | $$| $$  | $$| $$$$$         | $$ $$/$$ $$| $$$$$$$$| $$ $$ $$| $$$$$$$$| $$ /$$$$| $$$$$   | $$$$$$$/
| $$____/ | $$__  $$ \____  $$ \____  $$| $$      | $$  | $$| $$  | $$| $$__/         | $$  $$$| $$| $$__  $$| $$  $$$$| $$__  $$| $$|_  $$| $$__/   | $$__  $$
| $$      | $$  | $$ /$$  \ $$ /$$  \ $$| $$    $$| $$  | $$| $$  | $$| $$            | $$\  $ | $$| $$  | $$| $$\  $$$| $$  | $$| $$  \ $$| $$      | $$  \ $$
| $$      | $$  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$$$$$$/| $$$$$$$$      | $$ \/  | $$| $$  | $$| $$ \  $$| $$  | $$|  $$$$$$/| $$$$$$$$| $$  | $$
|__/      |__/  |__/ \______/  \______/  \______/  \______/ |_______/ |________/      |__/     |__/|__/  |__/|__/  \__/|__/  |__/ \______/ |________/|__/  |__/

 /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/ 

  _____                   _      _   _                                   _                         __                                                         _   _                  
 |_   _|                 | |    | | | |                                 | |                       / _|                                                       | | (_)              _  
   | |  _ __  _ __  _   _| |_   | |_| |__   ___    _ __  _   _ _ __ ___ | |__   ___ _ __     ___ | |_    _   _  ___  _   _ _ __     ___  _ __   ___ _ __ __ _| |_ _  ___  _ __   (_) 
   | | | '_ \| '_ \| | | | __|  | __| '_ \ / _ \  | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|   / _ \|  _|  | | | |/ _ \| | | | '__|   / _ \| '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \      
  _| |_| | | | |_) | |_| | |_   | |_| | | |  __/  | | | | |_| | | | | | | |_) |  __/ |     | (_) | |    | |_| | (_) | |_| | |     | (_) | |_) |  __/ | | (_| | |_| | (_) | | | |  _  
 |_____|_| |_| .__/ \__,_|\__|   \__|_| |_|\___|  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|      \___/|_|     \__, |\___/ \__,_|_|      \___/| .__/ \___|_|  \__,_|\__|_|\___/|_| |_| (_) 
             | |                                                                                          __/ |                         | |                                          
             |_|                                                                                         |___/                          |_|                                          

1. View Passcodes
2. Update Passcodes
3. Create New Passcode
4. Delete Passcodes
5. Update Passcode Manager Access Code
6. Exit The Passcode Manager
7. Exit The Entire Program
    ''')
def enter_key_and_confirm():
    correct = False
    while not correct:
        access_code = input(console_text("[Please enter the key to decrypt the passcode]: ", '\33[0;35m'))
        while not valid(access_code, "1234567890-=~!@#$%^&*()_+qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "):
            access_code = input("[Key must only contain characters on a standard English keyboard, please enter the key again]: ")
        if decrypt(passcode_dictionary["test"], int(generate_key_from_string(access_code))) != 1:
            print(console_text(f'The password entered is not correct, please try again.', "\033[0;31m"))
            print()
        else:
            correct = True
    return access_code
def view_passcode(passcode_dictionary, passcode_availability_data):
    bike_num = input(console_text("[Which bikes' passcode would you like to check? (separate number by space, e.g. 12 42 43]: ", '\33[0;32m'))
    valid_input = False
    while not valid_input:
        while not valid(bike_num, '0123456789 '):
            bike_num = input(console_text(f"[Please only input valid bikes]", '\33[0;33m'))
        for num in bike_num.strip().split(" "):
            if f'{int(num):02}' not in passcode_availability_data:
                bike_num = input(console_text(f"[Please only input valid bikes]", '\33[0;33m'))
                break
        valid_input = True
    bike_num_array = bike_num.strip().split(" ")
    keye = generate_key_from_string(enter_key_and_confirm())
    for bike in bike_num_array:
        bike_code= passcode_dictionary[f'{int(bike):02}']
        bike_code_final = decrypt(int(bike_code), int(keye))
        print(console_text(f'\n Bike {int(bike):02d}\'s passcode is \033[0;36m{bike_code_final:04d}\033[00m',"\033[0;32m"), end='')
    print('\n-------------------------')
    print()
def update_passcode(passcode_availability_data, passcode_raw_data):
    string_number = input(console_text("[Please enter which bike's passcode you want to update]: ", '\33[0;32m'))
    while not valid(string_number, '0123456789') or f'{string_number:02}' not in passcode_availability_data:
        string_number = input(console_text("[Bike number does not exists, please enter a valid bike number]: ", '\33[0;33m'))
    number = int(string_number)

    string_passcode = input(console_text(f"[Please enter the passcode you want to create for bike {number:02}]", '\33[0;35m'))
    while not valid(string_passcode, '0123456789') or len(string_passcode) > 4 or len(string_passcode) < 4:
        string_passcode = input(f"[Please enter a 4 digit number only, try again]: ")
    keyed = generate_key_from_string(enter_key_and_confirm())
    string_passcode_encrypted = encrypt(int(string_passcode), int(keyed))
    new_data = []
    for line in passcode_raw_data:
        if line.split(',')[0] == 'test':
            new_data.append(line)
        elif number != int(line.split(',')[0]):  # append if it is not the number
            new_data.append(line)
        else:
            new_data.append(f'{number:02}, {string_passcode_encrypted}\n')
    with open('watermelon_juice.csv', mode='w') as file:
        file.writelines(new_data)
    print(console_text('Passcode Updated', '\33[0;33m'))
    print('-------------------------')
    print()
    return f'{number:02}', string_passcode_encrypted
def create_passcode(passcode_availability_data, passcode_raw_data):
    string_number = input(console_text("[Please enter the bike you want to create the passcode for]: ", "\33[0;32m"))
    while not valid(string_number, '0123456789') or f'{string_number:02}' in passcode_availability_data:
        string_number = input(console_text("[Please input a bike number that does not exist]: ", '\33[0;33m'))
    number = int(string_number)

    string_passcode = input(console_text(f"[Please enter the passcode you want to create for bike {number}]", "\33[0;32m"))
    while not valid(string_passcode, '0123456789') or len(string_passcode) > 4 or len(string_passcode) < 4:
        string_passcode = input(console_text(f"[Please ONLY enter a 4 digit number, try again]: ", '\33[0;33m'))

    keyede = generate_key_from_string(enter_key_and_confirm())

    string_passcode_encrypted = encrypt(int(string_passcode), int(keyede))

    with open('watermelon_juice.csv', mode='w') as file:
        file.writelines(passcode_raw_data)
    print(console_text('Passcode Added', '\33[0;33m'))
    print('-------------------------')
    print()

    return f'{number:02}', string_passcode_encrypted
def delete_passcode(passcode_availability_data, passcode_raw_data):
    string_number = input(console_text("[Please enter which bike's passcode you want to delete]: ", '\33[0;32m'))
    while not valid(string_number, '0123456789') or f'{string_number:02}' not in passcode_availability_data:
        string_number = input(console_text("[Bike number does not exists, please enter a valid bike number]: ", '\33[0;33m'))
    number = int(string_number)
    new_data = []
    for line in passcode_raw_data:
        if line.split(',')[0] == 'test':
            new_data.append(line)
        elif number != int(line.split(',')[0]):  # append if it is not the number
            new_data.append(line)
    with open('watermelon_juice.csv', mode='w') as file:
        file.writelines(new_data)
    print(console_text('Passcode Deleted', '\33[0;33m'))
    print('-------------------------')
    print()
    return f'{string_number:02}'
def input_and_check_current_passcode(passcode_hashed):
    current_passcode = input(console_text("[Please enter your current access code]: ", '\33[0;32m'))
    error_count = 3

    while sha256(current_passcode.encode('utf-8')).hexdigest() != passcode_hashed and error_count != 0: #check if the user knows the current passcode
        current_passcode = input(console_text(f"[Wrong password entered, {error_count} more tries before exiting passcode manager]", "\33[0;31m"))
        print('error-1')
        error_count -= 1

    return True if error_count == 0 else current_passcode
def update_passcode_manager_access_code(passcode_dictionary):
    new_passcode = ''
    new_passcode = input(console_text("[Please enter your new access code]: ", '\33[0;32m'))
    confirmed_new_passcode = input(console_text("[Please confirmed your passcode]: ", '\33[0;33m'))
    while new_passcode != confirmed_new_passcode:
        print(console_text("[Passcodes did not match, please try again.]", '\33[0;31m'))
        print(" ")
        new_passcode = input(console_text("[Please enter your new access code]: ", '\33[0;32m'))
        confirmed_new_passcode = input(console_text("[Please confirmed your passcode]: ", '\33[0;33m'))

    passcode_hashed = sha256(new_passcode.encode('utf-8')).hexdigest()

    with open('access_code.txt', mode='w') as file:
        file.writelines(passcode_hashed)

    print(console_text("Access code changed successfully", "\33[0;32m"))
    print("-------------------------------------")
    print()
    return new_passcode, passcode_hashed

#functions for loading passcode data (encrypted)
def load_passcode_raw_data():
    with open('watermelon_juice.csv', mode ='r') as f:
        passcode_raw_data = f.readlines()
    return passcode_raw_data
def load_passcode_dictionary(passcode_raw_data):
    passcode_dictionary= {}
    for item in passcode_raw_data: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',')

        #unpacking
        name = data_separated[0]
        passcoded = data_separated[1]

        #add to passcode_dictionary(a dictionary)
        passcode_dictionary[name] = passcoded
    return passcode_dictionary
def load_passcode_availability_data(passcode_raw_data):
    passcode_availability_data = []
    for item in passcode_raw_data: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',')
        passcode_availability_data.append(data_separated[0])
    return passcode_availability_data

######################################################################################

program_running = True
normal_mode = True #initialize and keep track which mode software is running in
bike_data_raw = load_bike_raw_data() #load raw csv data for bike price into memory
bike_price_data = load_bike_price_data_data(bike_data_raw) #load bike price dictionary into memory
available_bike_data = load_bike_availability_data(bike_data_raw) #load the name of the available bikes as a list
passcode_hashed = load_passcode_hashed()
passcode_loaded = False

while program_running:
    menu()
    while normal_mode: #while in normal mode
        if bike_input_check_secret_entered(bike_price_data, available_bike_data, passcode_hashed): #ask what bike user wants to check. Turn off normal mode when secret code is entered
            normal_mode = False


    secret_menu()
    if not passcode_loaded:
        passcode_raw_data = load_passcode_raw_data()
        passcode_dictionary = load_passcode_dictionary(passcode_raw_data)
        passcode_availability_data = load_passcode_availability_data(passcode_raw_data)

    while not normal_mode:
        option = input_num_in_range(console_text("Enter your Option Here (1 - 7): ", "\33[0;36m"),console_text("Please only enter numbers from 1 to 7, try again: ", "\33[0;33m"), 1,7)
        if option == 1:
            view_passcode(passcode_dictionary, passcode_availability_data)
        elif option == 2:
            update_bike_data = update_passcode(passcode_availability_data, passcode_raw_data)
            passcode_dictionary[update_bike_data[0]] = update_bike_data[1]
            passcode_availability_data.append(update_bike_data[0])
        elif option == 3:
            new_bike_data = create_passcode(passcode_availability_data, passcode_raw_data)
            passcode_dictionary[new_bike_data[0]] = new_bike_data[1]
            passcode_availability_data.append(new_bike_data[0])
            passcode_raw_data.append(f'{new_bike_data[0]}, {new_bike_data[1]}\n')
        elif option == 4:
            deleted_bike_data = delete_passcode(passcode_availability_data, passcode_raw_data)
            passcode_availability_data.remove(f'{deleted_bike_data:02}')
        elif option == 5:
            new_passcode_raw_data = []
            b = input_and_check_current_passcode(passcode_hashed)
            if b == True:
                normal_mode = True
                print("normal mode activated")
            else:  # current_passcode, new_passcode]
                a = update_passcode_manager_access_code(passcode_dictionary)
                passcode_hashed = a[1]
                for key in passcode_dictionary.keys():
                    new_passcode_raw_data.append(f'{key}, {encrypt(decrypt(passcode_dictionary[key], int(generate_key_from_string(b))), int(generate_key_from_string(a[0])))}\n')
                    passcode_dictionary[key] = encrypt(decrypt(passcode_dictionary[key], int(generate_key_from_string(b))),int(generate_key_from_string(a[0])))
            passcode_raw_data = new_passcode_raw_data

            with open('watermelon_juice.csv', mode='w') as file:
                file.writelines(passcode_raw_data)
        elif option == 6:
            normal_mode = True#function that receives the mode as input and executes the function to perform that mode
        else:
            for i in range(200):
                print('\n')
            print("Program Successfully Shutted Down!")
            normal_mode = True
            program_running = False
