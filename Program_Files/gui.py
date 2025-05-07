import tkinter as tk
from tkinter import ttk, messagebox
from RSA_Functions import RSA_Encrypt, RSA_Decrypt, Encryption_Preparation
import json
from RSA_Core import Generate_Keys

def user_interface(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText):

    Private_Keys_History = []

    def Encryption():
        plaintext = input_text.get("1.0", tk.END).strip()

        if not plaintext:
            messagebox.showerror("Error", "The input box is empty. Please insert the plaintext to encrypt.")
            return

        plaintext = Encryption_Preparation(plaintext)

        if any(block >= PublicKey[1] for block in plaintext):
            messagebox.showerror("Encryption Error", "One or more blocks are too large for the current key. Please generate larger keys.")
            return

        ciphertext = RSA_Encrypt(plaintext, PublicKey)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, json.dumps(ciphertext))

    def Decryption():
        input_str = PrivateKeyInput.get().strip()

        if input_str:                           # Prepares the input key for decryption
            input_str = input_str.strip("()")
            d_str, n_str = input_str.split(",")
            d = int(d_str.strip())
            n = int(n_str.strip())
            PrivateKeyIn = (d, n)
        else:
            PrivateKeyIn = PrivateKey  # Uses the default key unless otherwise selected

        # Gets the input text
        ciphertext_str = input_text.get("1.0", tk.END).strip()

        if not ciphertext_str:
            messagebox.showerror("Error", "The input box is empty. Please insert the ciphertext to decrypt.")
            return

        try:
            ciphertext = json.loads(ciphertext_str)
        except json.JSONDecodeError:
            messagebox.showerror("Error", "The ciphertext is not valid JSON. Please make sure it's correctly formatted. '[x, x, ...]'")
            return

        try:
            decrypted_text = RSA_Decrypt(ciphertext, PrivateKeyIn)
            if decrypted_text == "Error":
                output_text.delete("1.0", tk.END)
                messagebox.showerror("Decryption Error", f"Incorrect key, impossible to decrypt.")
            else:      
                decrypted_text = decrypted_text.replace('\x00', '').strip()
                output_text.delete("1.0", tk.END)
                output_text.insert(tk.END, decrypted_text)
        except Exception as e:
            messagebox.showerror("Decryption Error", f"An error occurred during decryption:\n{str(e)}")

    def Regenerate_Keys():
        nonlocal PublicKey, PrivateKey, PublicKeyText, PrivateKeyText

        PublicKey, PrivateKey, PublicKeyText, PrivateKeyText = Generate_Keys()

        # Update the labels
        public_label.config(text=PublicKeyText)
        private_label.config(text=PrivateKeyText)

        Private_Keys_History.append(str(PrivateKey))
        PrivateKeyInput['values'] = Private_Keys_History  # update the values
        PrivateKeyInput.current(len(Private_Keys_History)-1)  # choose the last one

    def Cleaning():
        input_text.delete("1.0", tk.END)
        output_text.delete("1.0", tk.END)

    def AreYouSure():
        rUsure = tk.Toplevel()      # Are you sure window
        rUsure.geometry("240x80")

        tk.Label(rUsure, text = "Are you sure you want to exit the program?").grid(column = 0, row = 0, columnspan = 2, pady= 10)
        tk.Button(rUsure, text = "Yes", command = gui.destroy).grid(column = 0, row = 1)        # Yes Button (For exiting)
        tk.Button(rUsure, text = "No", command = rUsure.destroy).grid(column = 1, row = 1)      # No Button (For exiting)

    gui = tk.Tk()
    gui.title("RSA Encryption Interface")
    gui.geometry("750x250")
    gui.configure(bg = "#7DECF5")

    tk.Label(gui, text="Please insert the message:", bg = "#2C6D72", relief = "solid", borderwidth = 3).grid(column = 0, row = 0, pady = 5, padx = 100, ipady = 2, ipadx = 2)
    input_text = tk.Text(gui, height=9, width=40)
    input_text.grid(column = 0, row = 1, rowspan = 3, padx = 5)     # Input Box (Left)

    tk.Button(gui, text = "Encrypt", command= Encryption).grid(column = 1, row = 1, padx = 3)           # Encryption Button
    tk.Button(gui, text = "Decrypt", command= Decryption).grid(column = 1, row = 2, padx = 3, pady = 5) # Decryption Button
    tk.Button(gui, text = "Clean", command = Cleaning).grid(column = 1, row = 3, padx = 3)              # Clean Button
    tk.Button(gui, text = "Exit", command = AreYouSure).grid(column = 1, row = 4, padx = 3, pady = 10)  # Exit Button

    tk.Label(gui, text="Output message", bg = "#2C6D72", relief = "solid", borderwidth = 3).grid(column = 2, row = 0, pady = 5, ipady = 2, ipadx = 2)
    output_text = tk.Text(gui, height=9, width=40)
    output_text.grid(column = 2, row = 1, rowspan = 3, padx = 5)    # Output Box (Right)

    Keys_Info = tk.Frame(gui, relief = "solid", borderwidth = 3)
    Keys_Info.grid(column = 0, row = 4, rowspan = 2, pady = 5)

    tk.Button(Keys_Info, bg = "lightgray", text = "Regenerate Keys", command = Regenerate_Keys).grid(column = 0, row = 0, rowspan = 2, padx = 4)    # Regenerate keys Button
    public_label = tk.Label(Keys_Info, text=PublicKeyText, borderwidth=0)
    public_label.grid(column=1, row=0, pady=3, padx=10)

    private_label = tk.Label(Keys_Info, text=PrivateKeyText, borderwidth=0)
    private_label.grid(column=1, row=1, padx=10)

    history_frame = tk.Frame(gui, bg="#7DECF5")
    history_frame.grid(column=2, row=4, pady=10)        # Keys history frame

    tk.Label(history_frame, text = "Select Decryption Key", bg = "#7DECF5", borderwidth = 0).grid(column = 0, row = 0)

    PrivateKeyInput = ttk.Combobox(history_frame, values = Private_Keys_History, width = 37)
    PrivateKeyInput.grid(column = 0, row = 1)
    Private_Keys_History.append(str(PrivateKey))
    PrivateKeyInput['values'] = Private_Keys_History
    PrivateKeyInput.current(0)

    gui.mainloop()