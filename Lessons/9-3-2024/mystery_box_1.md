![image](https://github.com/user-attachments/assets/739fad56-44bf-4072-88d5-89b1e724d83b)

```.py
def mystery_box1(msg:str, lowered:bool):
    upper_to_lower = { #dictionary to turn uppercase into lowercase
        "A": "a",
        "B": "b",
        "C": "c",
        "D": "d",
        "E": "e",
        "F": "f",
        "G": "g",
        "H": "h",
        "I": "i",
        "J": "j",
        "K": "k",
        "L": "l",
        "M": "m",
        "N": "n",
        "O": "o",
        "P": "p",
        "Q": "q",
        "R": "r",
        "S": "s",
        "T": "t",
        "U": "u",
        "V": "v",
        "W": "w",
        "X": "x",
        "Y": "y",
        "Z": "z"
    }
    original_string = msg #orignal string
    lower = validation_bool(str(lowered)) #validate if the supposed boolean entered is a boolean
    new_string = '' #new string to output because python cant modify strings

    if lower: #if outside so only need to do if once
        for i in range(len(original_string)-1, -1, -1): #iterates string backwards
            if original_string[i] in upper_to_lower: #check if a letter is uppercase
                new_string += upper_to_lower[original_string[i]]
            else:
                new_string += original_string[i]
    else:
        for i in range(len(original_string)-1, -1, -1): #iterates string backwards
            new_string += original_string[i]

    print(new_string)

mystery_box1("Hello", True)
mystery_box1("Hello", False)
```

![image](https://github.com/user-attachments/assets/c7b5362a-f538-41d6-bed2-eabf0b413823)
