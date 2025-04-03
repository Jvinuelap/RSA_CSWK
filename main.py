from gui import user_interface
from RSA_Core import Generate_Keys

if __name__ == "__main__":
    PublicKey, PrivateKey, PublicKeyText, PrivateKeyText = Generate_Keys()
    user_interface(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText)

"""
Posible solutions to decrypting with incorrect message

Option 2: Use try/except + Ascii validations -> if not (32 <= ord(char) <= 126):
                                                    raise ValueError("Non-ASCII printable character")

"""