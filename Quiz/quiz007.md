# Quiz 007

## Paper Solution
![image](https://github.com/user-attachments/assets/b72ddc17-cb8c-4885-9c8e-db995e1527e4)

## Code
```.py
x = [5, 10, -3, 8, 11]

sorting = True
while sorting:
    sorting = False
    for j in range(len(x) - 1):
        if x[j] > x[j+1]: #compare with the next number in list
            sorting = True

            #swap x[j] with x[j+1]
            T = x[j]
            x[j] = x[j+1]
            x[j+1] = T

print(x) #output x sorted
```

## Proof of Work
![image](https://github.com/user-attachments/assets/ac4c22a0-4080-41db-b5c5-412590c95b03)


## Flow Diagram
