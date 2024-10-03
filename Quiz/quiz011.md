# Quiz 011

## Paper Solution
![image](https://github.com/user-attachments/assets/e8003c6c-23b8-40a1-a726-4e2227f8149f)

## Code
```.py
def quiz011(month:str):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    month_lowered = ''
    for letter in month:
        i = 0
        while letter != alphabet[i]:
            i += 1
        month_lowered += alphabet[i % 26]
    offset_and_day = {
        "january": [0,31],
        "february": [3,28],
        "march": [4,31],
        "april": [0,30],
        "may": [2,31],
        "june": [5,30],
        "july": [0,31],
        "august": [3,31],
        "september": [6,30],
        "october": [1,31],
        "november": [4,30],
        "december": [6,31],
    }
    output = ''
    days = ['Mo','Tu','We','Th','Fr','Sa','Su']
    month_data = offset_and_day[month_lowered]
    for i in range(1, month_data[1]):
        output += f'{days[(i-1+month_data[0])%7]} {i} '
    return output

print(quiz011('march'))
```
## Proof of Work
![image](https://github.com/user-attachments/assets/5a2eb210-fb3f-481d-92bc-1d5be7153ba4)

## Flow Diagram
![image](https://github.com/user-attachments/assets/9e110911-4de6-4e91-8996-02eb131b1a1b)
