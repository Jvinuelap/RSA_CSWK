import tkinter as tk
from tkinter import messagebox
from RSA_Functions import is_prime, Generate_Prime, mod_inverse, RSA_Encrypt, RSA_Decrypt
import json

def user_interface(e, d, n, PublicKey, PrivateKey):

    def Encryption():
        plaintext = input_text.get("1.0", tk.END).strip()  # Obtener texto de la entrada
        ciphertext = RSA_Encrypt(plaintext, e, n)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, json.dumps(ciphertext))

    def Decryption():
        ciphertext = json.loads(input_text.get("1.0", tk.END).strip())
        decrypted_text = RSA_Decrypt(ciphertext, d, n)
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

    tk.Label(gui, text = PublicKey, bg = "#7DECF5", borderwidth = 0).grid(column = 0, row = 4, pady = 5, padx = 10)
    tk.Label(gui, text = PrivateKey, bg = "#7DECF5", borderwidth = 0).grid(column = 0, row = 5, padx = 10)

    tk.Button(gui, text = "Clean", command = Cleaning).grid(column = 1, row = 3, padx = 5)

    gui.mainloop()
