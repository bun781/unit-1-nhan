![image](https://github.com/user-attachments/assets/25ff393a-717e-477b-98e5-827bac5fe5f8)# Quiz 006

## Paper Solution

## Code
```.py
from random import randint

pass_no_special_char = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM' #search up string when no special char
pass_with_special_char = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()`~-_=+{}|:\"<>?[]\\;',./" #search up string when  special char

def generate_10_passwords(length:int, char_included:bool):
    password_list = [] #list to store generated password
    end_code = "\033[00m"
    green = "\33[0;31m"
    if char_included: #check if want special char in password or not 
        for i in range(10): #genrate 10
            current_password = f'{green}'
            for j in range(length): #repeat for every character until password length is reached
                current_password += pass_with_special_char[randint(0, len(pass_with_special_char) - 1)] #choose random character from string
            password_list.append(current_password)
            current_password += f'{end_code}'
            print(current_password)
    else:
        for i in range(10):
            current_password = f''
            for j in range(length):
                current_password += pass_no_special_char[randint(0, len(pass_no_special_char)  - 1)] #choose random character from string
            password_list.append(current_password)
            print(current_password)

generate_10_passwords(20, True)
```

## Proof of Work
![image](https://github.com/user-attachments/assets/7dcdb351-b9ec-4244-9054-5ccb324ce7c4)

## Flow Chart
![image](https://github.com/user-attachments/assets/053172c4-dee5-47d8-b3ed-5f25b6da67a4)


