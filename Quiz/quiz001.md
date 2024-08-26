# Quiz 001

## Paper Solution
<img src = "https://github.com/user-attachments/assets/c021b3ca-4522-4e8f-a271-62be517ba44b" width = "300">

## Code
```.py
#Take input and split into words
inputString = str(input("Input your string: "))
splitString = inputString.split(" ")

#Generate output per word and print on same line
for wordBlock in splitString:
    if len(wordBlock) <= 2:
        print(wordBlock, end=" "),
    else:
        print(f"{wordBlock[0]}{len(wordBlock) - 2}{wordBlock[-1]}", end=" ")
```

## Proof of Work
<img src = "https://github.com/user-attachments/assets/56811ac3-e433-4746-837e-8cba54496463">
