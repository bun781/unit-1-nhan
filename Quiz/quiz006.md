# Quiz 005

## Paper Solution

## Code
```.py
from random import randint

pass_no_special_char = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
pass_with_special_char = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()`~-_=+{}|:\"<>?[]\\;',./"

def generate_10_passwords(length:int, char_included:bool):
    password_list = []
    end_code = "\033[00m"
    green = "\33[0;31m"
    if char_included:
        for i in range(10):
            current_password = f'{green}'
            for j in range(length):
                current_password += pass_with_special_char[randint(0, len(pass_with_special_char) - 1)]
            password_list.append(current_password)
            current_password += f'{end_code}'
            print(current_password)
    else:
        for i in range(10):
            current_password = f''
            for j in range(length):
                current_password += pass_no_special_char[randint(0, len(pass_no_special_char)  - 1)]
            password_list.append(current_password)
            print(current_password)

generate_10_passwords(20, True)
```

## Proof of Work
![image](https://github.com/user-attachments/assets/7dcdb351-b9ec-4244-9054-5ccb324ce7c4)

## Flow Chart
