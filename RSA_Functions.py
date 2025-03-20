import random

def is_prime(x):
    """Verifies if the number is primer or not."""
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def Generate_Prime(minimum, maximum):
    while True:
        num = random.randint(minimum, maximum)
        if is_prime(num):
            return num
        
def mod_inverse(e, phi):
    """Returns the modular inverse of e modulo phi using the Extended Euclidean Algorithm."""
    def extended_gcd(a, b):
        """Extended Euclidean Algorithm. Returns (gcd, x, y) such that ax + by = gcd(a, b)."""
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = extended_gcd(b % a, a)
            return (g, y - (b // a) * x, x)
    
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError(f"No modular inverse exists for e = {e} and phi = {phi}, as they are not coprime.")
    else:
        return x % phi  # Ensure the result is positive

def RSA_Encrypt(Plaintext, e, n):

    Ciphertext = []
    for i in Plaintext:
        AsciiPlaintext = ord(i)
        Ciphertext.append((AsciiPlaintext**e) % n)
        
    return Ciphertext

def ch_to_str(Characters):

    string = ''.join(Characters)

    return string

def RSA_Decrypt(Ciphertext, d, n):

    PlaintextCh = []
    for i in Ciphertext:
        Asciiplaintext = pow(i, d, n)
        PlaintextCh.append(chr(Asciiplaintext))

    Plaintext = ch_to_str(PlaintextCh)

    return Plaintext
