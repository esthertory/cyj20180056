
p = 11
q = 13
n = p * q
phi_n = (p-1) * (q-1)

e = 7

d = 0
mod = 0
while True:
    d += 1
    mod = (e * d) % phi_n
    if mod == 1:
        break
# Encryption
# C = P^e mod n

plain = "Hello World"
plain_list = [ord(x) for x in plain]

print('plain text', plain_list)

cipher= []
for i in plain_list:
    x = (i ** e) % n
    cipher.append (int(x))
    
print('cipher text', cipher)
# Decryption
# P = C^d mod Decryption

decrypted = []
for i in cipher:
    x = (i ** d) % n
    decrypted.append(int(x))
print('decrypted text', decrypted)

decrypted_text = ''.join([chr(x) for x in decrypted])
print (decrypted_text)
