# Quiz 002

## Paper Solution
<img src = "https://github.com/user-attachments/assets/497a847f-b678-42a0-b2bc-429a3ccaae43" width = "300">


## Code
SL Test Case and Code
```.py
A = [30, 30, 30, 200]
B = [10, 5, -10, -180]

#for testing on a per-input basis:
#A = int(input("Please input the first number"))
#B = int(input("Please input the second number"))

for i in range(len(A)):
    if A[i] == 20 or B[i] == 20 or A[i] + B[i] == 20:
        print(f"A = {str(A[i])}" + f"; B = {str(B[i])}"),
        print(True)
    else:
        print(f"A = {str(A[i])}" + f"; B = {str(B[i])}")
        print(False)
```
HL Test Case and Code
```.py
A = [10, 30, 10, 25]
B = [20, 15, 5, -6]

results = False
for i in range(len(A)):
    if A[i] == 20 or B[i] == 20 or A[i] + B[i] == 20:
        results = True
        break
print(results)
```

## Proof of Work
<img src = "https://github.com/user-attachments/assets/ccf8535f-3df8-4f2d-8126-422f92a5df2f" width = "300">
<img src = "https://github.com/user-attachments/assets/47314147-7c06-479d-a3e6-b86efaf2ad3e" width = 300">

## Flow Chart
![image](https://github.com/user-attachments/assets/fa4bf0a6-9848-4a64-a88e-8d88aef6847d)
