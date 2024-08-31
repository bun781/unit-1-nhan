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
factorSum = 0
for fac in factor:
    factorSum += fac

#if sum of factor = num => num is a perfect number
if factorSum == num:
    print(f"{', '.join(map(str, factor))}, True") #map(function, iterable thing), apply a function to all objects in an iterable thing
else:
    print(f"{', '.join(map(str, factor))}, False")
```

## Proof of Work
<img src = "https://github.com/user-attachments/assets/0b4ba940-b29e-4176-810c-d0253e307e1a" width = "450">
<img src = "https://github.com/user-attachments/assets/b07f9741-89b5-4713-9192-6a2382c0f7fc" width = "450">

## Flow Chart
![image](https://github.com/user-attachments/assets/35970006-ca62-48a7-a939-d521788d0899)

