import math
import pandas as pd
import numpy as np

msg = input("Enter message to be encrypted: ")
key = list(input("Enter key: "))
key = [int(i) for i in key]
sub = ['x', 'y', 'z']
msg = msg.replace(" ", "")
rows = len(msg)/len(key)
rows = list(range(0,math.ceil(rows)))

if len(msg) < (len(key)*len(rows)):
        val = (len(key)*len(rows)) - len(msg)
        for i in range(0,val):
            msg = msg + sub[i%3]

msg = list(msg)
arr1 = np.asarray(msg)
arr1 = arr1.reshape((len(rows), len(key)), order='C')
df = pd.DataFrame(arr1, index=rows, columns=range(1,(len(key)+1)))

ciphertext = []
for v in key:
    ciphertext.append(df[v].tolist())

ciphertext = [item for sublist in ciphertext for item in sublist]
ciphertext = ''.join(ciphertext).upper()

print(ciphertext)
