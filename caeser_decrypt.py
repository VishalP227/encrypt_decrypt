def decrypt(text, key):

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z']

    letters = []
    key_values = []
    msg = ""

    for i in text:
        letters.append(i)


    for j in letters:
        for idx, value in enumerate(alpha):
            if j == alpha[idx]:
                idx -= key
                key_values.append(idx)
                break

    for k in key_values:
        msg += alpha[k]

    if key != 00:
        print(msg)


text = input("enter encrypted message: ")

for i in range(0, 25):
    key = int(input("enter key: "))
    decrypt(text, key)
    if key == 00:
        break
