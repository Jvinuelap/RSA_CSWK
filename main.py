from gui import main_menu
from RSA_Core import Generate_Keys

if __name__ == "__main__":
    PublicKey, PrivateKey, PublicKeyText, PrivateKeyText = Generate_Keys()
    main_menu(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText)

