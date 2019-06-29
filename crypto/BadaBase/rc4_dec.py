import base64

with open("ciphertext", "r") as encrypted_file:
    data = base64.b64decode(encrypted_file.read())
key = "The king of Sheshach shall drink after them"

S = range(256)
j = 0
out = []

#KSA Phase
for i in range(256):
    j = (j + S[i] + ord( key[i % len(key)] )) % 256
    S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = j = 0
for char in data:
    i = ( i + 1 ) % 256
    j = ( j + S[i] ) % 256
    S[i] , S[j] = S[j] , S[i]
    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

decrypted_text = ''.join(out)
with open('decrypted.txt', 'w') as decrypted_file:
    decrypted_file.write(decrypted_text)