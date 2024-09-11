#write a csv file
# with open('store_db.csv',mode='a') as f:
#     f.writelines(['banana,300\n'])

#read a csv file
with open('store_db.csv', mode = 'r') as f:
    data = f.readlines()

catalog = {}
for item in data:
    data_cleaned = item.strip() #get rid of \n
    data_separated = data_cleaned.split(',')

    #unpacking
    name = data_separated[0]
    price = data_separated[1]

    #add to catalog (dictionary)
    catalog[name] = int(price)

end_code = "\033[00m"
cyan = "\033[0;36m"
red = "\033[0;31m"
terminated = False
while not terminated:
    flavour = input(f'{cyan}What flavour do you want?[Press X to exit, W to add new flavor]{end_code}: ')
    flavour = flavour.lower() #convert to lowercase

    if flavour == 'x':
        terminated = True
    elif flavour == 'w':
        #1. Ask user name of the new flavour
        #2. Check that the new name is not in the catalog
        #3. If name ok, ask for price, check if price is int
        #4. with name and price, write in append mode to the csv file
        #5. celebrate (print out the catalog
        name_valid = False #name valid or not
        name = input("What flavour would you like to add?: ")
        name = name.lower()
        while not name_valid:
            if name in catalog:
                name = input("Pleaes input a name that is not in the catalog: ")
            else:
                name_valid = True

        price_valid = False #price valid or not
        price = input("Input your price: ")  # input price
        while not price_valid:
            if price.isdigit():
                price_valid = True
            else:
                Price = input("Please input your price, integers please:")

        with open('store_db.csv',mode='a') as f:
            f.writelines(["\n",name,",", price])


    elif flavour in catalog:
        print(f'{flavour.title()} = ¥{catalog[flavour]}')
    else:
        exit(f"{red}Flavour not found{end_code}")

exit(f"{red}Thank you and come back again{end_code}")
