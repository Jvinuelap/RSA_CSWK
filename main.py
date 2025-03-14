from RSA_Functions import Generate_Prime, mod_inverse

p = Generate_Prime(100, 100000)
q = Generate_Prime(100, 100000)

print(f"p: {p}")
print(f"q: {q}")

e = 65537
phi_n = (p-1)*(q-1)
d = mod_inverse(e, phi_n)

print(f"The modular inverse of {e} modulo {phi_n} is: {d}")
print(f"The modular inverse of {e} modulo {phi_n} is: {d}")