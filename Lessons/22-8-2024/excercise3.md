# Write a program to sort alphabetically three names entered by the user. Note: Assume that only the first letter of names are the same. 

## Code
Sorting with the list can be a function. But since we are only dealing with 3 names, and I am not sure how to do it, the code is as follows:
```.py
#array to compare
compareArray = [list(input(f"Enter name {i}: ")) for i in range(3)]

#alphabet_dict = {chr(i): i - 97 for i in range(97, 123)}, method I learnt from chatGPT
rankTable = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
    'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16,
    'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}
rankedArray = [[] for _ in range(26)]

#sorting
for name in compareArray:
    firstLet = name[0]
    value = rankTable[firstLet]
    rankedArray[value].append(name)
rankedArray = [sublist for sublist in rankedArray if sublist] #if there exist a sublist, keep it.
for i in range(len(rankedArray)):
    temptArray = [[] for _ in range(26)]
    for name in rankedArray[i]:
        secondLet = name[1]
        value = rankTable[secondLet]
        temptArray[value] = name
    temptArray = [sublist for sublist in temptArray if sublist]
    rankedArray[i] = temptArray

#print words
words = [''.join(name) for sublist in rankedArray for name in sublist]
print("The names ranked in alphabetical order are: ")
for i in range(len(words)):
    print(f"{i+1}. " + words[i])
```

## Sample Output
![image](https://github.com/user-attachments/assets/f4ff5b1a-0dc5-40ea-b6e4-00db26dea6b7)











