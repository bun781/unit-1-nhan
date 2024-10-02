# Quiz 009

## Paper Solution

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
![image](https://github.com/user-attachments/assets/60e5f59f-e536-4b7d-b2dd-c974db0bdcbb)

