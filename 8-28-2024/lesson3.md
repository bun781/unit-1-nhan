```.py
range(start, end, steps)

#num form 10 to 100, even
range(10, 101, 2)

#all odd numbers between 1000 and 100
range(999, 99, -2)
```
# warm up
```.py
#Given N -> show alll factors of N
number = (input("Input your number: "))

#Validate that user entered number:
for letter in number:
    if letter not in '0123456789':
        print("Number not valid, try again")
        exit()

number = int(number)
for i in range(2, number - 1):
    if number % i == 0:
        print(f"{i} is a factor of {number}")
```

# kidMath thing
```.py
#print menu
print('''
Welcome to kidsMath :)
Menu:
1. Show a multiplication table
2. Show the factors
3. Count up to the number by steps
4. Find the iterations to reduce a number"
''')

def checkDigit(string, validation, error_message):
    for letter in string:
        if letter not in validation:
            print(error_message)
            return False
    return True

#ask for option
option = input("Please input your option: ")
while not checkDigit(option, '1234', "Option not valid, numbers from 1 to 4 only"):
    option = input("Please input your option: ")
option = int(option)

#option 1 input menu
if option == 1:
    print("Option 1: Show a multiplication table") #show function

    #input and validation
    num1 = input("Input the multiplication table you like to see (1-9): ")
    while not checkDigit(num1, '123456789', "Option not valid, numbers from 1 to 9 only"):
        num1 = input("Input the multiplication table you like to see (1-9): ")
    num1 = int(num1)

    #show multiplication table
    for i in range(1, 11):
        print(f"{num1} * {i} = {num1 * i}")

#option 2 input menu
if option == 2:
    print("Option 2: Show the factors")

    #input and validation
    num2 = input("Input your number: ")
    while not checkDigit(num2, '0123456789', "Only numbers!"):
        num2 = input("Input your number: ")
    num2 = int(num2)

    #function
    print(f"1 is a factor of {num2}")
    for i in range(2, num2 - 1):
        if num2 % i == 0:
            print(f"{i} is a factor of {num2}")
    print(f"{num2} is a factor of {num2}")

#option 3 input step
if option == 3:
    print("Option 3: Count up to a number by steps")

    #input and validation
    num3 = input("Input your number: ")
    while not checkDigit(num3, '0123456789', "Only numbers!"):
        num3 = input("Input your number: ")
    num3 = int(num3)

    step = input("Steps: ")
    while not checkDigit(step, '0123456789', "Only numbers!"):
        step = input("Steps: ")
    step = int(step)

    #print
    for i in range(0, num3, step):
        print(i)

if option == 4:
    print("Option 3: Count up to a number by steps")

    #input and validation
    num4 = input("Input your number: ")
    while not checkDigit(num4, '0123456789', "Only numbers!"):
        num4 = input("Input your number: ")
    cIteration = 1
    iterationCount = 0
    while num4 != 0 and len(num4) > 1:
        iterationCount += 1
        for digit in num4:
            cIteration *= int(digit)
        num4 = str(cIteration)
    print(iterationCount)
```
