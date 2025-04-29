from gui import user_interface
from RSA_Core import Generate_Keys

if __name__ == "__main__":
    PublicKey, PrivateKey, PublicKeyText, PrivateKeyText = Generate_Keys()
    user_interface(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText)
