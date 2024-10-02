# Quiz 014

# Paper Solution

# Code
```.py
def quiz014(n:int):
    door = '0'*n
    for i in range(1,n+1):
        new_door = ''
        for j in range(1, n+1):
            if j % i == 0:
                if door[j-1] == '0':
                    new_door += '1'
                else:
                    new_door += '0'
            else:
                new_door += door[j-1]
        door = new_door
    sum_opened = 0
    for i in range(len(door)):
        if door[i] == '1':
            sum_opened += 1
    return sum_opened

print(quiz014(10))
print(quiz014(100))
print(quiz014(200))
print(quiz014(5678))
```
# Proof of Work
![image](https://github.com/user-attachments/assets/4477e6d6-33fc-4e96-bd05-0f336acfc46a)

# Flow Diagram
![Uploading image.png…]()
