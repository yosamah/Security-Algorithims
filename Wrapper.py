import OneTimePad
import elgammal
import railFence

plaintext1 = "86"
plaintext2 = "17820305457150318"

key1 = "65"
key2 = 3
xa = 3
k = 5
q = 202
# One Time Pad
cipher1 = OneTimePad.otpEncryption(plaintext1, key1)

# rail fence
cipher2 = railFence.encryptRailFence(key2, plaintext2)

chunks = [3,1,2,2,2,3,2,2]
last_start = 0
arr = list()
for i in range(len(chunks)):
    arr.append(cipher2[last_start:last_start+chunks[i]])
    last_start += chunks[i]



# ElGamal
result = ""
for i in range(len(arr)):
    result += chr(elgammal.elGamalDecryption(xa, q, int(cipher1), int(arr[i]))) + " "

print(result)

