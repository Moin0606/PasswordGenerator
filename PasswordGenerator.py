
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb


def generate_password():
    len_str = length_entry.get()
    
    try:
        len_int = int(len_str)
        list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
        selected_char = random.sample(list_of_chars, len_int)
        
       
        pass_str = "".join(selected_char)
        pass_label.config(text=pass_str)

       
        print("Generated Password is:", pass_str, "\n")

    except ValueError:
       
        mb.showerror("Invalid Input", "Please enter a valid integer for password length.")


def reset():
    length_entry.delete(0, END)
    pass_label.config(text="")


if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("Random Password Generator ")
    guiWindow.geometry("500x450+400+200")
    guiWindow.config(bg="#ADD8E6")
    heading_frame = Frame(guiWindow, bg="#7B68EE")
    entry_frame = Frame(guiWindow, bg="#ADD8E6")
    button_frame = Frame(guiWindow, bg="#ADD8E6")
    result_frame = Frame(guiWindow, bg="#ADD8E6")
    heading_frame.pack(fill="both")
    entry_frame.pack(pady=10)
    button_frame.pack(pady=10)
    result_frame.pack(pady=10)

    heading = Label(
        heading_frame,
        text=" PASSWORD GENERATOR",
        font=("Bahnschrift SemiBold", "17"),
        bg="#90EE90",
        fg="#FF0000"
    )

   
    subheading = Label(
        heading_frame,
        text="Enter the Length of the Password:",
        font=("Bahnschrift SemiBold", "14"),
        bg="#90EE90",
        fg="#FFFFFF"
    )

   
    heading.pack(pady=10)
    subheading.pack(fill="both")

    length_entry = Entry(
        entry_frame,
        font=("Times New Roman", "12"),
        width=20
    )

   
    length_entry.grid(row=0, column=0, padx=10, pady=2, sticky=W)

    get_pass = Button(
        button_frame,
        text="Get Password",
        font=("Bahnschrift SemiBold", "12"),
        width=14,
        bg="#32CD32",
        fg="#FFFFFF",
        activebackground="#90EE90",
        activeforeground="#FFFFFF",
        relief=GROOVE,
        command=generate_password
    )

   
    clear_all = Button(
        button_frame,
        text="Reset",
        font=("Bahnschrift SemiBold", "12"),
        width=14,
        bg="#FF0000",
        fg="#FFFFFF",
        activebackground="#8B0000",
        activeforeground="#FFFFFF",
        relief=GROOVE,
        command=reset
    )

    
    get_pass.grid(row=0, column=0, padx=5, pady=2)
    clear_all.grid(row=0, column=1, padx=5, pady=2)

   
    pass_label = Label(
        result_frame,
        text="",
        font=("Consolas", "15", "bold"),
        bg="#E6E6FA",
        fg="#000000"
    )

    
    pass_label.pack()
    guiWindow.mainloop()
