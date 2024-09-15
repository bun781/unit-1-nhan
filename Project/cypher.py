original = 2139
key = 1453
binary_original = str(bin(original)[2:].zfill(12))
binary_key = str(bin(key)[2:].zfill(12))
print(f"orignal: {binary_original}")
print(f'key: {binary_key}')
round_1 = ''
for i in range(12): #xor orignal and key
    round_1 += '0' if binary_original[i] == binary_key[i] else '1'
#divide into 4 blocks
#shift 4 blocks into 1 of 16 possible combinations
round_2 = []
divided_key = []
for i in range(0,12,4):
    round_2.append(round_1[i:i+4])
for i in range(0,12,4):
    divided_key.append(binary_key[i:i+4])
shift = key % 3
new_round_2 = round_2[shift:] + round_2[:shift]
round_3 = ['','','']
for i in range(3):
    for j in range(4):
        round_3[i] += '0' if new_round_2[i][j] == divided_key[i][j] else '1'
round_4 =''
round_4 += "".join(let for let in round_3)
round_5 = int(round_4, 2)
