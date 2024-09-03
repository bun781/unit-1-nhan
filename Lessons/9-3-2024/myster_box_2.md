![image](https://github.com/user-attachments/assets/99909ac2-dff3-4aa3-9617-540d9bd767ba)

```.py
def mystery_box2(input_string:str):
    has_at = False #check if input_string is a valid email address
    for l in input_string:
        if l == '@':
            has_at = True

    user_name = '' #create string for username
    domain_name = '' #create string for domain name
    name_switched = False #check if loop has passed the @

    if not has_at: #will exit if email is not valid
        print('Not a valid email address, program exiting...')
        exit()
    else:
        for l in input_string:
            if not name_switched: #if not passed the @ yet, add the char to user_name
                if l == '@': #check if char is @
                    name_switched = True
                else: #else add char to username
                    user_name += l
            elif name_switched: #if passed username then just add the char directly to domain name
                domain_name += l

    #return output
    return user_name, domain_name

print(mystery_box2("john.doe@gmail.com"))
```

![image](https://github.com/user-attachments/assets/4748070d-7d30-4624-b050-762522ce821d)
