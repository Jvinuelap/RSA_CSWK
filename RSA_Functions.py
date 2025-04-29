import random

def is_prime(x): # Checks if a number is prime
    
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

def Generate_Prime(minimum, maximum): # Generates a random prime number
    while True:
        num = random.randint(minimum, maximum)
        if is_prime(num):
            return num
        
def mod_inverse(e, phi):
    # Returns the modular inverse of e modulo phi using the Extended Euclidean Algorithm.
    def extended_gcd(a, b):
        # Extended Euclidean Algorithm. Returns (gcd, x, y) such that ax + by = gcd(a, b).
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

def RSA_Encrypt(Plaintext, PublicKey):

    e, n = PublicKey

    try:
        Ciphertext = []
        for i in Plaintext:
            Ciphertext.append((int(i)**e) % n)      # Applies modulo of n
    except:
        Ciphertext = "Wrong format, impossible to encrypt."

    return Ciphertext

def RSA_Decrypt(Ciphertext, PrivateKey):
    d, n = PrivateKey

    Splitted = []

    try:
        for i in Ciphertext:
            # Decrypt and convert to a 9-character string, padding with leading zeros if necessary
            Concat_plaintext = str(pow(i, d, n)).rjust(9, '0')
            blocks = [Concat_plaintext[i:i+3] for i in range(0, len(Concat_plaintext), 3)]

            # Delete '000' blocks from the beginning
            while blocks and blocks[0] == '000':
                blocks.pop(0)

            Splitted.extend(blocks)

        Plaintext = ''
        for code in Splitted:  # Ensures all the characters are printable (incorrect key)
            char = chr(int(code))
            if not (32 <= ord(char) <= 126):
                return "Error"
            Plaintext += char

    except Exception as e:
        return "Incorrect Key, Impossible to decrypt."

    return Plaintext


def Encryption_Preparation(Plaintext):
    PlaintextAscii = []
    for i in Plaintext:
        PlaintextCh = str(ord(i))               # Converts to Ascii code each character

        while(len(PlaintextCh) < 3):            # Adds zeros in the left to ascii codes which have less than 3 digits
            PlaintextCh = '0' + PlaintextCh
        
        PlaintextAscii.append(PlaintextCh)
        
    PlaintextAscii3Ch = ''
    PlaintextAscii3ChList = []
    concat = 0

    for i in PlaintextAscii:
        
        if(concat < 3):
            PlaintextAscii3Ch += i          # Joins the characters in groups of 3
            concat += 1

            if(len(PlaintextAscii3Ch) == 9):        
                PlaintextAscii3ChList.append(PlaintextAscii3Ch)     # If a group is formed, it is added to the list to be encrypted
                PlaintextAscii3Ch = ''
                concat = 0
            
    if PlaintextAscii3Ch:
        PlaintextAscii3ChList.append(PlaintextAscii3Ch)             # Any remaining elements are added to the list to be encrypted
        
    for i in range(len(PlaintextAscii3ChList)):
        PlaintextAscii3ChList[i] = PlaintextAscii3ChList[i].rjust(9, '0')   # Adds zeros at the left so that every element has 9 digits

    return [int(i) for i in PlaintextAscii3ChList]      #Converts each block of nunbers in integers

