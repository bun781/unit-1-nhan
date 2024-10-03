# Quiz 009

## Paper Solution
![image](https://github.com/user-attachments/assets/42c27a58-c56d-4b12-8560-bb62c189060e)

## Code
```.py
def quiz009(data:str, shift:int):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = ''
    for letter in data:
        if letter == " ":
            output += ' '
        else:
            i = 0
            while letter != alphabet[i]:
                i += 1
            output += alphabet[(i+shift) % 26]
    return output
print(quiz009('hello world', 13))
```

## Proof of Work
![image](https://github.com/user-attachments/assets/62f10771-dd69-4461-84ee-f4fbe9c8017a)

## Flow Chart
![image](https://github.com/user-attachments/assets/03de0898-fa21-482d-84fe-4c28a4642da3)



