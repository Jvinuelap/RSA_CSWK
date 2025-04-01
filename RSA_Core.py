from RSA_Functions import Generate_Prime, mod_inverse, RSA_Encrypt, RSA_Decrypt, Encryption_Preparation

def Generate_Keys():
    p = Generate_Prime(100, 100000)
    q = Generate_Prime(100, 100000)
    e = 65537
    n = p * q
    phi_n = (p-1)*(q-1)
    d = mod_inverse(e, phi_n)

    PublicKey = (e, n)
    PrivateKey = (d, n)

    PublicKeyText = f"Public key: ({e},{n})"
    PrivateKeyText = f"Private key: ({d},{n})"

    return PublicKey, PrivateKey, PublicKeyText, PrivateKeyText
