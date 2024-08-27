This is what the input originally looked like, but creating 3 objects and 1 more object is unecessary
```.py
#Enter Name and turn into Array
name1 = list(input("Enter the first name: "))
name2 = list(input("Enter the second name: "))
name3 = list(input("Enter the third name: "))

comparisonArray = [name1, name2, name3]
```

One interesting code piece I learnt was that I can call ASCII characters by using the ``chr()`` function (from ChatGPT)
```.py
alphabet_dict = {chr(i): i - 97 for i in range(97, 123)} #method I learnt from chatGPT
```
A more comprehensive version could be:
```.py
  firstLet = name[0]
  value = rankTable[firstLet]
```
