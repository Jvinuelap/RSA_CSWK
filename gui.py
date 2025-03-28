import tkinter as tk
from tkinter import messagebox
from RSA_Functions import RSA_Encrypt, RSA_Decrypt, Encryption_Preparation
import json

def user_interface(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText):

    def Encryption():
        plaintext = input_text.get("1.0", tk.END).strip()  # Obtener texto de la entrada
        plaintext = Encryption_Preparation(plaintext)
        ciphertext = RSA_Encrypt(plaintext, PublicKey)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, json.dumps(ciphertext))

    def Decryption():

        input_str = PrivateKeyInput.get("1.0", "end").strip()

        if input_str:
            print("Hey")
            input_str = input_str.strip("()")
            d_str, n_str = input_str.split(",")
            d = int(d_str.strip())
            n = int(n_str.strip())
            print(f"d: {d}, n: {n}")
            PrivateKeyIn = (d, n)
            ciphertext = json.loads(input_text.get("1.0", tk.END).strip())
            decrypted_text = RSA_Decrypt(ciphertext, PrivateKeyIn)
        else:
            ciphertext = json.loads(input_text.get("1.0", tk.END).strip())
            decrypted_text = RSA_Decrypt(ciphertext, PrivateKey)

        decrypted_text = decrypted_text.replace('\x00', '').strip()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)

    def Cleaning():
        input_text.delete("1.0", tk.END)
        output_text.delete("1.0", tk.END)

    gui = tk.Tk()
    gui.title("RSA Encryption Interface")
    gui.geometry("750x240")
    gui.configure(bg = "#7DECF5")

    tk.Label(gui, text="Please insert the message:", bg = "#2C6D72", relief = "solid", borderwidth = 3).grid(column = 0, row = 0, pady = 5, padx = 100, ipady = 2, ipadx = 2)
    input_text = tk.Text(gui, height=9, width=40)
    input_text.grid(column = 0, row = 1, rowspan = 3, padx = 5)

    tk.Button(gui, text = "Encrypt", command= Encryption).grid(column = 1, row = 1, padx = 5)
    tk.Button(gui, text = "Decrypt", command= Decryption).grid(column = 1, row = 2, padx = 5, pady = 5)

    tk.Label(gui, text="Output message", bg = "#2C6D72", relief = "solid", borderwidth = 3).grid(column = 2, row = 0, pady = 5, ipady = 2, ipadx = 2)
    output_text = tk.Text(gui, height=9, width=40)
    output_text.grid(column = 2, row = 1, rowspan = 3, padx = 5)

    tk.Label(gui, text = PublicKeyText, bg = "#7DECF5", borderwidth = 0).grid(column = 0, row = 4, pady = 5, padx = 10)
    tk.Label(gui, text = PrivateKeyText, bg = "#7DECF5", borderwidth = 0).grid(column = 0, row = 5, padx = 10)

    tk.Button(gui, text = "Clean", command = Cleaning).grid(column = 1, row = 3, padx = 5)

    PrivateKeyInput = tk.Text(gui, height=1, width=30)
    PrivateKeyInput.grid(column=2, row=4, rowspan=2, pady=5)




    gui.mainloop()
