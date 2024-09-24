from Tools.i18n.msgfmt import generate


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
print(generate_key_from_string('I love biking so much!'))