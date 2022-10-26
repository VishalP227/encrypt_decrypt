import math
import numpy as np
import pandas as pd

encrypted_msg = input("Enter encrypted message: ")
encrypted_msg = encrypted_msg.lower()
key = list(input("Enter key: "))
key = [int(i) for i in key]
num = int(len(encrypted_msg)/len(key))
count = 0
var = {}
for i in key:
    word = list(encrypted_msg[count:count+num])
    var[i] = word
    count += num

df = pd.DataFrame(var, index=range(0,num))
msg_list = []
for i in list(range(0,num)):
    msg_list.append(df.iloc[i].tolist())

decrypted_message = [item for sublist in msg_list for item in sublist]
decrypted_message = ''.join(decrypted_message)

print(decrypted_message)
