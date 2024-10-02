# Quiz 015

## Paper Solution

## Code
```.py
def quiz015(words:list):
    letter_sum = 0
    count = 0
    for word in words:
        count += 1
        for letter in word:
            if letter != " ":
                letter_sum += 1
    average = letter_sum/count
    return float(f'{average:.02}')
print(quiz015(['hello', 'main']))
print(quiz015(['Peru', 'France', 'Nepal']))
print(quiz015(['Computer Science', 'Art']))
print(quiz015(['one', 'two']))
```
## Proof of Work
![image](https://github.com/user-attachments/assets/019d52f1-07d9-4c6d-87d7-993339342db6)

## Flow Diagram
![image](https://github.com/user-attachments/assets/35d3f806-3bf4-46db-835f-10d28bff2c5b)
