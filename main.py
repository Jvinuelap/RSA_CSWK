from gui import main_menu
from RSA_Core import Generate_Keys

if __name__ == "__main__":
    PublicKey, PrivateKey, PublicKeyText, PrivateKeyText = Generate_Keys()
    main_menu(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText)

"""
Posible solutions to decrypting with incorrect message

Option 1: Validate with "padding" or special signature -> Before encrypt, add a key word like (RSA_MSG: ).
Later, while decrypting, check that the key word exists

Option 2: Use try/except + Ascii validations -> if not (32 <= ord(char) <= 126):
                                                    raise ValueError("Non-ASCII printable character")

Option 3: Check if the characters are printable (Letters, numbers, spaces and puntuation)

"""