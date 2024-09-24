#validate input function
from hashlib import sha256
#function to validate input
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
    for i in range(0,15,5):
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
    for i in range(0,15,5):
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
def console_text(message:str,color:str):
    end = "\033[00m"    #stop further message from accidentally being color
    return f"{color}{message}{end}" #return the colored message as f string

def load_passcode_hashed():
    with open('access_code.txt', mode='r') as file:
        passcode_hashed = file.readlines()[0]
    return passcode_hashed

def bike_input_check_secret_entered(bike_price, available_bike, passcode_hashed):
    accepted = False
    secret_access = False

    text = f"Welcome to Karuizawa Rentals, please check the rental rate per hour by entering a valid bike number. To check for available bikes, enter X: "
    color = "\33[0;35m"
    while not accepted:
        bike_num_str = input(console_text(text, color))  # ask for input
        print(sha256(bike_num_str.encode('utf-8')).hexdigest())
        print(passcode_hashed)
        if sha256(bike_num_str.encode('utf-8')).hexdigest() == passcode_hashed: #the string is the sha265 hashed version of the passcode (for security reasons)
            return True
        elif bike_num_str in 'xX':
            string_available_bike = ''
            for num, bike in enumerate(available_bike):
                if num % 20 == 19: #make 20 columns
                    string_available_bike += f"{bike},\n"
                else:
                    string_available_bike += f"{bike}, "
            print("The available bikes are: ")
            print(string_available_bike)
            print("Above are the available bikes.") #make long list less confusing for smaller displays
            print('-----------------------')
            break
        elif not valid(bike_num_str, '0123456789'): #check if input is number
            text = f"Please enter a valid bike number, please try again: "
            color = "\33[0;33m"
            continue  #go back to asking for input

        if f'{bike_num_str:02}' not in available_bike: #check if number is valid
            text = f"Please enter a valid bike number"
            color = "\33[0;33m"
            continue #go back to asking for input
        else:
            bike_num = int(bike_num_str)
            accepted = True #end the loop
    if accepted:
        print(console_text(f'\nYou can rent bike {bike_num:02} for ¥{bike_price[f"{bike_num:02}"]}/hour',"\33[0;32m"))  # bike_price[f"{bike_num:02} returns the price from the dictionary. Not made a variable to save memory.
        print("-------------")  # for clarity #print the bike rental rate


def load_bike_raw_data():
    with open('bike_data.csv', mode ='r') as f:
        bike_data_raw = f.readlines()
    return bike_data_raw
def load_bike_price_data(bike_data_raw):
    bike_price = {}
    for item in bike_data_raw: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',')

        #unpacking
        name = data_separated[0]
        price = data_separated[1]

        #add to bike_data (a dictionary)
        bike_price[name] = int(price)
    return bike_price

def load_bike_availability_data(bike_data_raw):
    available_bike = []
    for item in bike_data_raw: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',') #split the data into separate bike number and price
        available_bike.append(data_separated[0]) #add the bike number to the availability list
    return available_bike

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
    ''')
def option_select_and_do():
    global normal_mode
    option = input_num_in_range(console_text("Enter your Option Here (1 - 6): ","\33[0;36m"), console_text("Please only enter numbers from 1 to 6, try again: ","\33[0;33m"), 1, 6)
    if option == 1:
        view_passcode(passcode, available_passcode)
    elif option == 2:
        update_passcode(available_passcode, passcode_data)
    elif option == 3:
        create_passcode(available_passcode, passcode_data)
    elif option == 4:
        delete_passcode(available_passcode, passcode_data)
    elif option == 5:
        if not update_passcode_manager_access_code(passcode_hashed):
            normal_mode = True
    elif option == 6:
        normal_mode = True

#generate key from string
def view_passcode(passcode, available_passcode):
    bike_num = input(f"Enter bike number would you like to view the password for: ")
    while f'{int(bike_num):02}' not in available_passcode:
        bike_num = input(f"Please only input valid bikes")
    bike_code= passcode[f'{int(bike_num):02}']
    print(passcode[f'{int(bike_num):02}'])
    print(f'{int(bike_num):02}')
    confirmed = False
    while not confirmed:
        access_code = input("Please enter the key to decrypt the passcode: ")
        while not valid(access_code, "1234567890-=~!@#$%^&*()_+qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "):
            access_code = input("Key must only contain characters on a standard English keyboard, please enter the key again: ")

        confirmed_input = input("Are you sure this is the right key? Entering the wrong key will return the wrong password. Press Y to confirm, press X to enter the key again: ")
        while not valid(confirmed_input, 'xXyY'):
            confirmed_input = input("Please enter X or Y")
        if confirmed_input in 'yY':
            confirmed = True
        else: #equivalent to if confirmed_input = 'xX'
            continue
    key = generate_key_from_string(access_code)
    bike_code_final = decrypt(int(bike_code), int(key))
    print(console_text(f'the bike passcode is {bike_code_final}', "\033[0;32m"))
    print('-------------------------')
    access_code = '' #reset access code

def update_passcode(available_passcode, passcode_data):
    string_number = input("Please enter which bike's passcode you want to update: ")
    while not valid(string_number, '0123456789') or f'{string_number:02}' not in available_passcode:
        string_number = input("Bike number does not exists, please enter a valid bike number: ")
    number = int(string_number)

    string_passcode = input(f"Please enter the passcode you want to create for bike {number:02}")
    while not valid(string_passcode, '0123456789') or len(string_passcode) > 4 or len(string_passcode) < 4:
        string_passcode = input(f"Please enter a 4 digit number only, try again: ")

    confirmed = False
    while not confirmed:
        access_code = input("Please enter the key to encrypt the passcode (same as the passcode to access the password manager): ")
        while not valid(access_code,"1234567890-=~!@#$%^&*()_+qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "):
            access_code = input("Key must only contain characters on a standard English keyboard, please enter the key again: ")

        confirmed_input = input("Are you sure this is the right key? Entering the wrong key will return the wrong password. Press Y to confirm, press X to enter the key again: ")
        while not valid(confirmed_input, 'xXyY'):
            confirmed_input = input("Please enter X or Y")
        if confirmed_input in 'yY':
            confirmed = True
        else:  # equivalent to if confirmed_input = 'xX'
            continue
    key = generate_key_from_string(access_code)

    string_passcode_encrypted = encrypt(int(string_passcode), int(key))

    new_data = []

    for line in passcode_data:
        if number != int(line.split(',')[0]):  # append if it is not the number
            new_data.append(line)
        else:
            new_data.append(f'{number:02}, {string_passcode_encrypted}\n')
            print(f'{number:02}')
    passcode[f'{number:02}'] = string_passcode_encrypted

    with open('watermelon_juice.csv', mode='w') as file:
        file.writelines(new_data)
    print('Passcode Updated')
    print('-------------------------')

def create_passcode(available_passcode, passcode_data):
    string_number = input("Please enter which bike's passcode you want to create: ")
    while not valid(string_number, '0123456789') or f'{string_number:02}' in available_passcode:
        string_number = input("Please input a bike number, a number, not a string, that does not exist: ")
    number = int(string_number)

    string_passcode = input(f"Please enter the passcode you want to create for bike {number}")
    while not valid(string_passcode, '0123456789') or len(string_passcode) > 4 or len(string_passcode) < 4:
        string_passcode = input(f"Please enter a 4 digit number only, try again: ")
    confirmed = False
    while not confirmed:
        access_code = input("Please enter the key to encrypt the passcode (same as the passcode to access the password manager): ")
        while not valid(access_code,"1234567890-=~!@#$%^&*()_+qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "):
            access_code = input("Key must only contain characters on a standard English keyboard, please enter the key again: ")

        confirmed_input = input("Are you sure this is the right key? Entering the wrong key will return the wrong password. Press Y to confirm, press X to enter the key again: ")
        while not valid(confirmed_input, 'xXyY'):
            confirmed_input = input("Please enter X or Y")
        if confirmed_input in 'yY':
            confirmed = True
        else:  # equivalent to if confirmed_input = 'xX'
            continue
    key = generate_key_from_string(access_code)

    string_passcode_encrypted = encrypt(int(string_passcode), int(key))
    passcode_data.append(f'{number:02}, {string_passcode_encrypted}\n')

    available_passcode.append(f'{string_number:02}')


    with open('watermelon_juice.csv', mode='w') as file:
        file.writelines(passcode_data)
    print('Passcode Added')
    print('-------------------------')

def delete_passcode(available_passcode, passcode_data):
    string_number = input("Please enter which bike's passcode you want to delete: ")
    while not valid(string_number, '0123456789') or f'{string_number:02}' not in available_passcode:
        string_number = input("Bike number does not exists, please enter a valid bike number: ")
    number = int(string_number)
    new_data = []
    for line_no, line in enumerate(passcode_data):
        if number != int(line_no + 1):  # append if it is not the number
            new_data.append(line)

    available_passcode.remove(f'{string_number:02}')

    with open('watermelon_juice.csv', mode='w') as file:
        file.writelines(new_data)
    print('Passcode Deleted')
    print('-------------------------')

def update_passcode_manager_access_code(passcode_hashed):
    current_passcode = input("Please enter your current access code: ")
    error_count = 3

    while sha256(current_passcode.encode('utf-8')).hexdigest() != passcode_hashed and error_count != 0: #check if the user knows the current passcode
        current_passcode = input(f"Wrong password entered, please try again, {error_count} more tries before exiting passcode manager")
        error_count -= 1
        if error_count == 0:
            return True #normal mode is true

    if not normal_mode:
        new_passcode = input("Please enter your new access code: ")
        confirmed_new_passcode = input("Please confirmed your passcode: ")
        while new_passcode != confirmed_new_passcode:
            print("Passcodes did not match, please try again.")
            print(" ")
            new_passcode = input("Please enter your new access code: ")
            confirmed_new_passcode = input("Please confirmed your passcode: ")
        for key in passcode.keys():
            passcode[key] = encrypt(decrypt(passcode[key], int(generate_key_from_string(current_passcode))), int(generate_key_from_string(new_passcode)))

        passcode_hashed = sha256(new_passcode.encode('utf-8')).hexdigest()

        with open('access_code.txt', mode='w') as file:
            file.writelines(passcode_hashed)

        print("Access code changed successfully")
        print("-------------------------------------")

def load_passcode_raw_data():
    with open('watermelon_juice.csv', mode ='r') as f:
        passcode_data = f.readlines()
    return passcode_data

def load_passcode_dictionary(passcode_data):
    passcode = {}
    for item in passcode_data: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',')

        #unpacking
        name = data_separated[0]
        passcoded = data_separated[1]

        #add to passcode (a dictionary)
        passcode[name] = passcoded
    return passcode

def load_passcode_availability_data(passcode_data):
    available_passcode = []
    for item in passcode_data: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',')
        available_passcode.append(data_separated[0])
    return available_passcode



######################################################################################



normal_mode = True #keep track which mode software is running in
bike_data_raw = load_bike_raw_data()
bike_price = load_bike_price_data(bike_data_raw)
available_bike = load_bike_availability_data(bike_data_raw)
passcode_hashed = load_passcode_hashed()

passcode_loaded = False
while True:
    menu_loaded = False
    while normal_mode: #while in normal mode
        if not menu_loaded:
            menu()
            menu_loaded = True
        if bike_input_check_secret_entered(bike_price, available_bike, passcode_hashed): #ask what bike user wants to check. Turn off normal mode when secret code is entered
            normal_mode = False

    if not normal_mode:
        secret_menu()
        if not passcode_loaded: #only extract data to memory if in passcode manager to save resources
            passcode_data = load_passcode_raw_data()
            passcode = load_passcode_dictionary(passcode_data)
            available_passcode = load_passcode_availability_data(passcode_data)
    while not normal_mode:
        option_select_and_do() #function that receives the mode as input and executes the function to perform that mode
