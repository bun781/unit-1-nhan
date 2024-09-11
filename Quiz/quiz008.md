# Quiz 008

## Paper Solution
![image](https://github.com/user-attachments/assets/36f7570c-93b1-490c-98a6-d7b7ad96ca65)

## Code
HL Code:
```.py
def find_room(room_number:int):
    list_room = []
    room_count = 10
    floor_count = 10

    for i in range(1, floor_count + 1):
        for j in range(1, room_count + 1):
            list_room.append(f"-Room {i}F{j:02d}")

    for i in range(0, room_count * floor_count):
        list_room[i] = str(i + 1) + list_room[i]

    return list_room[room_count]

print(find_room(67))
print(find_room(100))
print(find_room(3))
```

SL Code:
```.py
list_room = []
room_count = 10
floor_count = 10

for i in range(1, floor_count + 1):
    for j in range(1, room_count + 1):
        list_room.append(f"-Room {i}F{j:02d}")

for i in range(0, room_count * floor_count):
    list_room[i] = str(i + 1) + list_room[i]

print("\n".join(list_room))
```

## Proof of Work
<img src = "https://github.com/user-attachments/assets/b8b429e6-8578-4dc7-83ed-1652af06ccba" width = "300">
<img src = "https://github.com/user-attachments/assets/2f624aa0-7e4f-4391-aae5-7d80c55dcfc8" width = "300">

## Flow Chart
![image](https://github.com/user-attachments/assets/b9ce5d17-a5aa-499d-9aa5-91179e7291aa)

