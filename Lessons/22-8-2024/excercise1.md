# Create a program that organizes from largest to smallest three heights in cms entered by the user.

## Code
```.py
userInput = input("Input your three numbers, separated by space")
userArray = [int(num) for num in userInput.split(" ")] # change string to int and put into an array
orderedArray = []

while userArray: #while userArray is empty (i have no clue why the syntax is like this)
    for currentNum in userArray[:]: #use a copy instead of userArray itself...
        if all(currentNum >= num for num in userArray): #a very not smart way to sort but because we only have 3 elements.
            orderedArray.append(currentNum)
            userArray.remove(currentNum)
print(orderedArray)
```
## Sample Output
![image](https://github.com/user-attachments/assets/d0d4599e-20a2-4ce8-bac3-1de8a2a09130)
