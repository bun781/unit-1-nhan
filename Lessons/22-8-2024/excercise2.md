#  Create a program that calculates the tax for a salary entered by the user following the table below

## Code
```.py
salary = float(input("Input your salary: "))
realSalary = 0

if salary <= 10000:
    tax = salary * 0.05
elif salary <= 50000:
    tax = 10000 * 0.05 + (salary - 10000) * 0.10
elif salary <= 100000:
    tax = 10000 * 0.05 + 40000 * 0.10 + (salary - 50000) * 0.15
else:
    tax = 10000 * 0.05 + 40000 * 0.10 + 50000 * 0.15 + (salary - 100000) * 0.25

print(f"The total tax is {tax}")
```
## Sample Output
![image](https://github.com/user-attachments/assets/5614f9c5-2937-4a59-8c9d-aabde99356ca)
