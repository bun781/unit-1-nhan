![image](https://github.com/user-attachments/assets/907c53b1-7b00-493a-9a35-14dea520199b)

```.py
def mystery_box3(a:int, b:int, c:int):
    if not check_input(str(a), '0123456789') or not check_input(str(b), '0123456789') or not check_input(str(c), '0123456789'):
        exit()
    smallest_possible_guess = 0
    if a < b:
        if a < c:
            smallest_possible_guess = a
        else:
            smallest_possible_guess = c
    elif b < c :
        smallest_possible_guess = b
    else:
        smallest_possible_guess = c

    biggest_possible_guess = a * b * c

    for i in range(smallest_possible_guess, biggest_possible_guess+1):
        if i % a == 0 and i % b == 0 and i % c == 0:
            return i
print(mystery_box3(8, 6, 2))
print(mystery_box3(18, 4, 7))
print(mystery_box3(5, 10, 7))
print(mystery_box3(5, 6, 3))
```

![image](https://github.com/user-attachments/assets/4b905ef3-058d-4f58-a35f-69a4c064d26c)
