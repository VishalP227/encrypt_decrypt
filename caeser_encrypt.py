def encrypt(text, key):

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z']

    letters = []
    key_values = []
    encrypt_msg = ""

    for i in text:
        letters.append(i)


    for j in letters:
        for idx, value in enumerate(alpha):
            if j == alpha[idx]:
                idx += key
                if idx > 25:
                    idx = idx-26
                key_values.append(idx)
                break

    for k in key_values:
        encrypt_msg += alpha[k]

    print(encrypt_msg)

text = input("Enter message: ")
key = int(input("Enter key: "))
encrypt(text, key)
