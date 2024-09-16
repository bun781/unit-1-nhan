# Quiz 004

## Paper Solution
<img src = "https://github.com/user-attachments/assets/50949128-b947-4b97-b9b4-57ac9c80e26b" width = "300">

## Code
```.py
num = int(input("Input your number"))
factor = []

#find list of factors
for i in range(1, num):
    if num % i == 0:
        factor.append(i)

#find the sum of factors
output_string = ''
factorSum = 0
for fac in factor:
    factorSum += fac
    output_string += f"{str(fac)}, "

#if sum of factor = num => num is a perfect number
if factorSum == num: #add whether the number is perfect or not
    output_string += "True"
else:
    output_string += "False"

print(output_string)
```

## Proof of Work
<img src = "https://github.com/user-attachments/assets/37b6d794-784c-43ab-b748-f00dd4a77225" width = "450">
<img src = "https://github.com/user-attachments/assets/5236393d-14c1-40e6-8105-cfb3f032cd4e" width = "450">

## Flow Chart
![image](https://github.com/user-attachments/assets/5f45d9c3-6fa4-4b50-a722-3d5f3ca4af3a)

