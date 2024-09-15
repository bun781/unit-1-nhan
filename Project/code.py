#validate input function
from hashlib import sha256
#function to validate input
def valid(string:str, validation:str):
    valid = True
    for letter in string:
        if letter not in validation: #loop through each character to see if they are valid or not
            valid = False
            break
    return valid
def input_num_in_range(start_text:str,error_text:str,lowest_option:int,highest_option:int):
    accepted = False
    a = start_text
    while not accepted:
        option_str = input(a)
        a = error_text
        if not valid(option_str, '01234567890'):
            continue

        option = int(option_str)

        if option < lowest_option or option > highest_option:
            text = error_text
        else:
            accepted = True

    return option
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
def bike_input_check_secret_entered():
    global accepted #let other functions know if number is accepted
    global bike_num#let other functions know about bike_num

    accepted = False
    secret_access = False

    lowest_bike_num = 1
    highest_bike_num = 203

    text = "Welcome to Karuizawa Rentals, please check the rental rate per hour by entering the bike number (01 - 203): "
    color = "\33[0;35m"
    while not accepted:
        bike_num_str = input(console_text(text, "\33[0;35m"))  # ask for input
        if sha256(bike_num_str.encode('utf-8')).hexdigest() == '2f691c60c6f1b2527a9d93d83da8f7cdf8cb538cca48f2741b641866abf14241': #the string is the sha265 hashed version of the passcode (for security reasons)
            secret_access = True
            break

        elif not valid(bike_num_str, '0123456789'): #check if input is number
            text = "Only whole numbers between 1 and 203, please try again: "
            color = "\33[0;33m"
            continue  #go back to asking for input

        bike_num = int(bike_num_str)  # convert input to integer

        if bike_num < lowest_bike_num or bike_num > highest_bike_num: #check if number is valid
            text = "Only whole numbers between 1 and 203, please try again: "
            continue #go back to asking for input
        else:
            accepted = True #end the loop
    return secret_access
def bike_output():
    # print the bike rental rate
    print(console_text(f'You can rent bike {bike_num:02} for ¥{bike_price[f"{bike_num:02}"]}/hour',"\33[0;32m"))  # bike_price[f"{bike_num:02} returns the price from the dictionary. Not made a variable to save memory.
    print("-------------") #for clarity #print the bike rental rate
def load_bike_data():
    global bike_price
    bike_price = {}
    with open('bike_data.csv', mode = 'r') as f:
        data = f.readlines()
    for item in data: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',')

        #unpacking
        name = data_separated[0]
        price = data_separated[1]

        #add to bike_data (a dictionary)
        bike_price[name] = int(price)

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
        view_passcode()
    elif option == 2:
        update_passcode()
    elif option == 3:
        create_passcode()
    elif option == 4:
        delete_passcode()
    elif option == 5:
        update_passcode_manager_access_code()
    elif option == 6:
        normal_mode = True

def view_passcode():
    print('1')
def update_passcode():
    print('1')
def create_passcode():
    print('1')
def delete_passcode():
    print('1')
def update_passcode_manager_access_code():
    print('1')

def load_passcode():
    global passcode
    passcode = {}
    with open('watermelon_juice.csv', mode = 'r') as f:
        data = f.readlines()
    for item in data: #repeat for every line in the csv
        data_cleaned = item.strip() #get rid of \n
        data_separated = data_cleaned.split(',')

        #unpacking
        name = data_separated[0]
        passcode = data_separated[1]

        #add to passcode (a dictionary)
        pass_code[name] = passcode


######################################################################################

normal_mode = True #keep track which mode software is running in
load_bike_data()
passcode_loaded = False
while True:
    menu_loaded = False
    while normal_mode: #while in normal mode
        if not menu_loaded:
            menu()
            menu_loaded = True
        if bike_input_check_secret_entered(): #ask what bike user wants to check. Turn off normal mode when secret code is entered
            normal_mode = False
        elif accepted:
            bike_output()

    if not normal_mode:
        secret_menu()
        if not passcode_loaded: #only extract data to memory if in passcode manager to save resources
            load_passcode()
    while not normal_mode:
        option_select_and_do() #function that receives the mode as input and executes the function to perform that mode










# bike


# check if user entered secret code




# passcode manager software

# menu screen

# create password

# replace password

# update password

# delete password
