# Quiz 010

## Paper Solution
![image](https://github.com/user-attachments/assets/291457ab-aaa1-4ee3-b690-97441c59d9c5)

## Code
```.py
def powersTen(input_string:str):
    for i in range(len(input_string)):
        if input_string[i] in '0123456789':
            number_index = i

    number = ''
    while input_string[number_index] in '0123456789':
        number += input_string[number_index]
        number_index += 1
    while input_string[number_index] in ' ': #while the current char is space
        number_index += 1

    unit = ''
    while input_string[number_index] not in ' ': #while not space
        unit += input_string[number_index]
        number_index += 1


    output_format =f'''
        {number} 000 000 000 000     Tera
        {number} 000 000 000         Giga
        {number} 000 000             Mega
        {number} 000                 kilo
        {number}                     {unit}
        0.00{number}                 mili
        0.000 00{number}             micro
        0.000 000 00{number}         nano
        0.000 000 000 00{number}     pico
        '''
    return output_format

print(powersTen('1 gram of salt'))
```
## Proof of Work
![image](https://github.com/user-attachments/assets/016a36da-e56c-4d2d-91fd-3c705f59530e)

## Flow Diagram
![image](https://github.com/user-attachments/assets/09cce614-33df-4b10-a9e6-05291df61cd5)

