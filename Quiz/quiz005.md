# Quiz 005

## Paper Solution
![image](https://github.com/user-attachments/assets/693817a2-6888-4f5d-9bfb-aa3a87b45bff)

## Code
SL Code
```.py
letter_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #get char by char_position % 26

input_string = "Computer SCIENCE"
sum_letters = 0
for letter in input_string:
    if letter in letter_string:
        sum_letters += letter_string.index(letter) % 26 + 1 #plus the value of the number, modulo is to find the value regardless of uppercase and lower case
    elif letter == ' ':
        sum_letters += -32 #from "Hello World" and "Computer SCIENCE", we can deduce that ' '  = -32
    else:
        print("Words and spaces only!!!")  #if a character is neither uppercase or lowercase letter, exit.
        exit()

print(sum_letters)
```

HL Code
```.py
letter_string_lower = "abcdefghijklmnopqrstuvwxyz" #string to help in finding value of a letter
letter_string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_string = "Math" #string to be ran through
sum_letters = 0 #keep track of the sum of the letters

for letter in input_string:
    if letter in letter_string_lower:
        sum_letters += letter_string_lower.index(letter) + 1 #plus the value of the number
    elif letter in letter_string_upper:
        sum_letters += letter_string_upper.index(letter) + 1344 #M + a + t + h = 1385, m + a + t + h = 42 => M = m + 1343 => Uppercase's value is lower case + 1343
    elif letter == ' ': #from "Hello World" and "Computer SCIENCE", we can deduce that ' '  = -32
        sum_letters += -32
    else:
        print("Words and spaces only!!!") #if a character is neither uppercase or lowercase letter, exit.
        exit()

print(sum_letters)
```


## Proof of Work
<img src = "https://github.com/user-attachments/assets/eff92f0c-9e8a-455d-9f1c-35c60c87b155" width = "300">
<img src = "https://github.com/user-attachments/assets/630f6d71-1b90-4b5d-bbdc-e91aa3bc2180" width = "300">

## Flow Chart
![image](https://github.com/user-attachments/assets/15ec05ec-9a59-4496-b22e-95f9b2e97272)


