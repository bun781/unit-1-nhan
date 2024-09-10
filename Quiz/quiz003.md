# Quiz 003

## Paper Solution
<img src = "https://github.com/user-attachments/assets/1a7bbf3e-c4a1-41c8-b5df-19e9f2c396ba" width = "300">

## Code 
```.py
proteinDict = { #dictionary for protein
    "A": "T",
    "G": "C",
    "T": "A",
    "C": "G",
}

inputString = "AGCT"
newString = "" #new string because strings in python can't be edited

#run through each letter in the input string and add the translated to the new string
for letter in inputString:
    newString += proteinDict[letter]

print(newString)
```
## Proof of Work
![image](https://github.com/user-attachments/assets/d8a166a3-993b-41ce-85df-f932646e862c)

## Flow Chart
![image](https://github.com/user-attachments/assets/076a2199-3628-4b55-8db3-4e2572514700)
