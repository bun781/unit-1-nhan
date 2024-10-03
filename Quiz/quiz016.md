# Quiz 016

## Paper Solution

## Boolean Circuit

## Code
```.py
def get_l3tt3r(msg:str):
    output = ''
    change_to_number = { #there were only suggestions for a e i o on the slides, but I needed to do it for all vowels, so I just chose 5.
        'a': '4',
        'e': '3',
        'i': '1',
        '0': '0',
        'u': '5',
        ' ': '_'
    }
    for letter in msg:
        if letter in change_to_number:
            output += change_to_number[letter]
        else:
            output += letter
    return output

print(get_l3tt3r('Hello World'))
print(get_l3tt3r('Why did I choose CS'))
print(get_l3tt3r('Remember the Figure Caption'))
```
## Proof of Work
![image](https://github.com/user-attachments/assets/5becc09c-4900-48e0-b873-3e4edd6ae3f5)

## Flow Diagram
![image](https://github.com/user-attachments/assets/52b0ece4-bfe4-49a4-b51c-66ecf41e9a01)
