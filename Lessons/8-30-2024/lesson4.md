# Given a base, print 100 chars
```.py
#input and check
base = input("Input your number (2 - 10): ")
for letter in base:
    if letter not in '0123456789':
        print('Integers only')
        exit()
base = int(base)
if 10 < base or 2 > base:
    print('Only integers between 2 and 10')
    exit()

#print
for i in range(100):
    print(i%base, end = ' ')
```

# An alternative method
```.py
k = 0
for num in range(100):
    print(k)
    k += 1
    if k == base:
        k = 0
```

# center justify
```.py
def centerJust(input1, len1, filler):
    s = input1
    for i in range(len1-len(input1)):
        if i % 2 == 0:
            s = filler + s
        else:
            s = s + filler
    return s

print(centerJust("hello", 10, "."))
```
Trace Table:

Step | base | k | output
0 | 3 | 0 | - | - 
1 | _ | _ | - | 0
2 | _ | 1 | _ | 0
...
