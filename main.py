from RSA_Functions import is_prime, Generate_Prime, mod_inverse, RSA_Encrypt, RSA_Decrypt
from gui import user_interface

p = Generate_Prime(100, 100000)
q = Generate_Prime(100, 100000)

print(f"p: {p}")
print(f"q: {q}")

e = 65537
n = p * q
phi_n = (p-1)*(q-1)
d = mod_inverse(e, phi_n)

print(f"The modular inverse of {e} modulo {phi_n} is: {d}")

PublicKey = (e, n)
PrivateKey = (d, n)

print(f"Public key: ({e},{n})")
PublicKeyText = f"Public key: ({e},{n})"
print(f"Private key: ({d},{n})")
PrivateKeyText = f"Private key: ({d},{n})"

Plaintext = 'Hello, RSA Encryption Here!'
print(f"\nMessage: {Plaintext}")
Ciphertext = RSA_Encrypt(Plaintext, PublicKey)
print(f"\nEncoded Message: {Ciphertext}")
Plaintext = RSA_Decrypt(Ciphertext, PrivateKey)
print(f"\nDecrypted Message: {Plaintext}")

user_interface(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText)
