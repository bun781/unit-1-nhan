![image](https://github.com/user-attachments/assets/ab09263c-baab-4e8e-9b58-c58c758a639f)

```.py
def mystery_box4(input_list:list):
    if not isinstance(input_list, list):
        print("Input lists only")
        exit()
    if len(input_list) < 7:
        print("Input list is too short")
        exit()
    for l in input_list:
        if str(l) not in '0123456789':
            print("Input positive integers only")
            exit()
    output_list = []
    total = 0
    for i in range(4):
        total += input_list[i]
        output_list.append(input_list[i])
    average = total / 5
    return average, output_list

print(mystery_box4([5, 6, 3, 8, 1, 7, 9]))
```

![image](https://github.com/user-attachments/assets/ff694e47-c745-4176-8179-d4a987d829c5)
