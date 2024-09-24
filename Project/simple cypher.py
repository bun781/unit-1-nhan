#in case something goes wrong with the encrypted database
def base_10_to_2_15_bits(base_10_number:int):
    base_2_number_string = ''
    if base_10_number == 0:
        base_2_number_string = '0'

    while base_10_number > 0:
        remainder = base_10_number % 2
        base_2_number_string = str(remainder) + base_2_number_string
        base_10_number = base_10_number // 2 #floor division to make sure number is always correct

    while len(base_2_number_string) < 15:
        base_2_number_string = "0" + base_2_number_string

    return base_2_number_string
def encrypt(original:int, key:int):
    binary_original = base_10_to_2_15_bits(original) #change into 15bit binary string (as 9999 is 14 bit, so +1 because 15 is more flexible)
    binary_key = base_10_to_2_15_bits(key)

    round_1 = ''
    for i in range(15): #xor orignal and key
        if binary_original[i] == binary_key[i]:
            round_1 += '0'
        else:
            round_1 += '1'

    round_2 = []
    divided_key = []
    for i in range(0,15,5): #split into 3 parts
        round_2.append(round_1[i:i+5])
    for i in range(0,15,5):
        divided_key.append(binary_key[i:i+5])
    shift = key % 3
    new_round_2 = round_2[shift:] + round_2[:shift] #shift the order of the partitions for the original string
    round_3 = ['','','']
    for i in range(3):
        for j in range(5):
            if new_round_2[i][j] == divided_key[i][j]: #nxor partition of original string with the corresponding partition of the key
                round_3[i] += '1'
            else:
                round_3[i] += '0'
    round_4 =''
    for let in round_3:
        round_4 += let
    round_5 = int(round_4, 2) #turn the binary string back into integer
    return round_5
def decrypt(encrypted:int, key:int):
    binary_encrypted = str(bin(encrypted)[2:].zfill(15))
    binary_key = str(bin(key)[2:].zfill(15))

    divided_binary_encrypted = []
    divided_binary_key = []
    for i in range(0,15,5):
        divided_binary_encrypted.append(binary_encrypted[i:i+5])
    for i in range(0,15,5):
        divided_binary_key.append(binary_key[i:i+5])


    divided_binary_encrypted_1 = ['','','']
    for i in range(3):
        for j in range(5):
            if divided_binary_encrypted[i][j] == divided_binary_key[i][j]:
                divided_binary_encrypted_1[i] += '1'
            else:
                divided_binary_encrypted_1[i] += '0'

    shift = key % 3
    new_divided_binary_encrypted_1 = divided_binary_encrypted_1[(3-shift):] + divided_binary_encrypted_1[:(3-shift)]
    original = ''
    for i in range(3):
        for j in range(5):
            if new_divided_binary_encrypted_1[i][j] == divided_binary_key[i][j]:
                original += '0'
            else:
                original += '1'
    print(int(original, 2))
def generate_key_from_string(input_string:str):
    value_string = "1234567890-=~!@#$%^&*()_+qwertyuiop[]\\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
    letter_product = 1
    for letter in input_string:
        letter_product *= (value_string.index(letter) + 1) #+1 to make sure no number is 0
    string_letter_product = str(letter_product)

    key_string = ''
    if len(string_letter_product) < 4:
        while len(string_letter_product) < 4:
            string_letter_product += "0"
        key_string += string_letter_product
    elif len(string_letter_product) > 4:
        key_string += string_letter_product[0:4] #get the first 4 values
    else: #when len(string_letter_product) = 4
        key_string += string_letter_product

    return key_string
with open('watermelon_juice.csv', mode ='r') as f:
    passcode_data = f.readlines()
new_data = []
for item in passcode_data: #repeat for every line in the csv
    data_cleaned = item.strip() #get rid of \n
    data_separated = data_cleaned.split(',')

    #unpacking
    name = data_separated[0]
    passcoded = data_separated[1]
    a = generate_key_from_string(#insert current key)
    new_data.append(f'{name}, {encrypt(int(passcoded), int(a))}\n')

with open('watermelon_juice.csv', mode='w') as file:
    file.writelines(new_data)
