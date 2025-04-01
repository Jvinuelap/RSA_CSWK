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
        ciphertext = RSA_Encrypt(plaintext, PublicKey)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, json.dumps(ciphertext))

    def Decryption():
        input_str = PrivateKeyInput.get().strip()

        if input_str:
            input_str = input_str.strip("()")
            d_str, n_str = input_str.split(",")
            d = int(d_str.strip())
            n = int(n_str.strip())
            PrivateKeyIn = (d, n)
        else:
            PrivateKeyIn = PrivateKey  # usa la clave original si no se pone una manualmente

        # Obtener el texto cifrado del campo
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
            decrypted_text = decrypted_text.replace('\x00', '').strip()
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, decrypted_text)
        except Exception as e:
            messagebox.showerror("Decryption Error", f"An error occurred during decryption:\n{str(e)}")

    def Regenerate_Keys():
        nonlocal PublicKey, PrivateKey, PublicKeyText, PrivateKeyText

        PublicKey, PrivateKey, PublicKeyText, PrivateKeyText = Generate_Keys()

        # Actualizar los labels
        public_label.config(text=PublicKeyText)
        private_label.config(text=PrivateKeyText)

        Private_Keys_History.append(str(PrivateKey))
        PrivateKeyInput['values'] = Private_Keys_History  # actualizar los valores
        PrivateKeyInput.current(len(Private_Keys_History)-1)  # seleccionar el último

    def Cleaning():
        input_text.delete("1.0", tk.END)
        output_text.delete("1.0", tk.END)

    gui = tk.Toplevel()
    gui.title("RSA Encryption Interface")
    gui.geometry("750x250")
    gui.configure(bg = "#7DECF5")

    tk.Label(gui, text="Please insert the message:", bg = "#2C6D72", relief = "solid", borderwidth = 3).grid(column = 0, row = 0, pady = 5, padx = 100, ipady = 2, ipadx = 2)
    input_text = tk.Text(gui, height=9, width=40)
    input_text.grid(column = 0, row = 1, rowspan = 3, padx = 5)     # Input Box (Left)

    tk.Button(gui, text = "Encrypt", command= Encryption).grid(column = 1, row = 1, padx = 3)           # Encryption Button
    tk.Button(gui, text = "Decrypt", command= Decryption).grid(column = 1, row = 2, padx = 3, pady = 5) # Decryption Button
    tk.Button(gui, text = "Clean", command = Cleaning).grid(column = 1, row = 3, padx = 3)              # Clean Button
    tk.Button(gui, text = "Exit", command = gui.destroy).grid(column = 1, row = 4, padx = 3, pady = 10)  # Exit Button

    tk.Label(gui, text="Output message", bg = "#2C6D72", relief = "solid", borderwidth = 3).grid(column = 2, row = 0, pady = 5, ipady = 2, ipadx = 2)
    output_text = tk.Text(gui, height=9, width=40)
    output_text.grid(column = 2, row = 1, rowspan = 3, padx = 5)    # Output Box (Right)

    Keys_Info = tk.Frame(gui, relief = "solid", borderwidth = 3)
    Keys_Info.grid(column = 0, row = 4, rowspan = 2, pady = 5)

    tk.Button(Keys_Info, bg = "lightgray", text = "Regenerate Keys", command = Regenerate_Keys).grid(column = 0, row = 0, rowspan = 2, padx = 4)
    public_label = tk.Label(Keys_Info, text=PublicKeyText, borderwidth=0)
    public_label.grid(column=1, row=0, pady=3, padx=10)

    private_label = tk.Label(Keys_Info, text=PrivateKeyText, borderwidth=0)
    private_label.grid(column=1, row=1, padx=10)

    history_frame = tk.Frame(gui, bg="#7DECF5")
    history_frame.grid(column=2, row=4, pady=10)

    tk.Label(history_frame, text = "Select Decryption Key", bg = "#7DECF5", borderwidth = 0).grid(column = 0, row = 0)

    PrivateKeyInput = ttk.Combobox(history_frame, values = Private_Keys_History, width = 37)
    PrivateKeyInput.grid(column = 0, row = 1)
    Private_Keys_History.append(str(PrivateKey))
    PrivateKeyInput['values'] = Private_Keys_History
    PrivateKeyInput.current(0)



def saved_keys_window():
    keys_gui = tk.Toplevel()
    keys_gui.title("Saved Keys")
    keys_gui.geometry("300x200")
    tk.Label(keys_gui, text="Here you can manage saved keys.", font=('Arial', 12)).pack(pady=20)
    # You can add functionality to load/display keys from a file here

def main_menu(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText):

    def AreYouSure():
        rUsure = tk.Toplevel()
        rUsure.geometry("240x80")

        tk.Label(rUsure, text = "Are you sure you want to exit the program?").grid(column = 0, row = 0, columnspan = 2, pady= 10)
        tk.Button(rUsure, text = "Yes", command = menu.destroy).grid(column = 0, row = 1)
        tk.Button(rUsure, text = "No", command = rUsure.destroy).grid(column = 1, row = 1)

    menu = tk.Tk()
    menu.title("Main Menu")
    menu.geometry("300x200")

    tk.Label(menu, text="Select an Option", font=('Arial', 14)).pack(pady=20)
    tk.Button(menu, text="RSA Interface", width=20, command=lambda: user_interface(PublicKey, PrivateKey, PublicKeyText, PrivateKeyText)).pack(pady=10)
    tk.Button(menu, text="Saved Keys", width=20, command=saved_keys_window).pack(pady=10)
    tk.Button(menu, text="Exit", width=20, command=AreYouSure).pack(pady=10)

    menu.mainloop()
 
